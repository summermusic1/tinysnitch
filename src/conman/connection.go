package conman

import (
	"fmt"
	"github.com/evilsocket/opensnitch/src/dns"
	"github.com/evilsocket/opensnitch/src/log"
	"github.com/evilsocket/opensnitch/src/netfilter"
	"github.com/evilsocket/opensnitch/src/netstat"
	"github.com/evilsocket/opensnitch/src/procmon"
	"github.com/google/gopacket/layers"
	"net"
	"os"
)

type Connection struct {
	Protocol string
	SrcIP    net.IP
	SrcPort  uint
	DstIP    net.IP
	DstPort  uint
	DstHost  string
	Entry    *netstat.Entry
	Process  *procmon.Process
	pkt      *netfilter.Packet
}

func Parse(nfp netfilter.Packet) *Connection {
	ipLayer := nfp.Packet.Layer(layers.LayerTypeIPv4)
	ipLayer6 := nfp.Packet.Layer(layers.LayerTypeIPv6)
	if ipLayer == nil && ipLayer6 == nil {
		log.Info("nil i fifth %s", nfp)
		return nil
	}
	if ipLayer == nil {
		ip, ok := ipLayer6.(*layers.IPv6)
		if ok == false || ip == nil {
			log.Info("not ok %s", nfp)
			return nil
		}
		if ip.SrcIP.IsLoopback() {
			// log.Info("loopy %s", nfp)
			return nil
		}
		if ip.SrcIP.IsMulticast() || ip.DstIP.IsMulticast() {
			// log.Info("multi %s", nfp)
			return nil
		}
		con, err := NewConnection6(&nfp, ip)
		if err != nil {
			log.Debug("%s", err)
			return nil
		} else if con == nil {
			log.Info("conless %s", nfp)
			return nil
		}
		return con
	} else {
		ip, ok := ipLayer.(*layers.IPv4)
		if ok == false || ip == nil {
			log.Info("not ok ipv6 %s", nfp)
			return nil
		}
		if ip.SrcIP.IsLoopback() {
			// log.Info("loopy ipv6 %s", nfp)
			return nil
		}
		if ip.SrcIP.IsMulticast() || ip.DstIP.IsMulticast() {
			// log.Info("multi ipv6 %s", nfp)
			return nil
		}
		con, err := NewConnection(&nfp, ip)
		if err != nil {
			log.Debug("ipv6 %s", err)
			return nil
		} else if con == nil {
			log.Info("conless ipv6 %s", nfp)
			return nil
		}
		return con
	}
}

func newConnectionImpl(nfp *netfilter.Packet, c *Connection) (cr *Connection, err error) {
	// no errors but not enough info neither
	if c.parseDirection() == false {
		return nil, nil
	}
	// 1. lookup uid and inode using /proc/net/(udp|tcp)
	// 2. lookup pid by inode
	// 3. if this is coming from us, just accept
	// 4. lookup process info by pid
	c.Entry = netstat.FindEntry(c.Protocol, c.SrcIP, c.SrcPort, c.DstIP, c.DstPort)
	if c.Entry == nil {
		return nil, fmt.Errorf("Could not find netstat entry for: %s", c)
	}
	pid := procmon.GetPIDFromINode(c.Entry.INode)
	if pid == -1 {
		return nil, fmt.Errorf("Could not find process id for: %s", c)
	}
	if pid == os.Getpid() {
		return nil, nil
	}
	c.Process = procmon.FindProcess(pid)
	if c.Process == nil {
		return nil, fmt.Errorf("Could not find process by its pid %d for: %s", pid, c)
	}
	return c, nil
}

func NewConnection(nfp *netfilter.Packet, ip *layers.IPv4) (c *Connection, err error) {
	c = &Connection{
		SrcIP:   ip.SrcIP,
		DstIP:   ip.DstIP,
		DstHost: dns.HostOr(ip.DstIP, ip.DstIP.String()),
		pkt:     nfp,
	}
	return newConnectionImpl(nfp, c)
}

func NewConnection6(nfp *netfilter.Packet, ip *layers.IPv6) (c *Connection, err error) {
	c = &Connection{
		SrcIP:   ip.SrcIP,
		DstIP:   ip.DstIP,
		DstHost: dns.HostOr(ip.DstIP, ip.DstIP.String()),
		pkt:     nfp,
	}
	return newConnectionImpl(nfp, c)
}

func (c *Connection) parseDirection() bool {
	ret := false
	for _, layer := range c.pkt.Packet.Layers() {
		if layer.LayerType() == layers.LayerTypeTCP {
			if tcp, ok := layer.(*layers.TCP); ok == true && tcp != nil {
				c.Protocol = "tcp"
				c.DstPort = uint(tcp.DstPort)
				c.SrcPort = uint(tcp.SrcPort)
				ret = true
			}
		} else if layer.LayerType() == layers.LayerTypeUDP {
			if udp, ok := layer.(*layers.UDP); ok == true && udp != nil {
				c.Protocol = "udp"
				c.DstPort = uint(udp.DstPort)
				c.SrcPort = uint(udp.SrcPort)
				ret = true
			}
		}
	}
	for _, layer := range c.pkt.Packet.Layers() {
		if layer.LayerType() == layers.LayerTypeIPv6 {
			if tcp, ok := layer.(*layers.IPv6); ok == true && tcp != nil {
				c.Protocol += "6"
			}
		}
	}
	return ret
}


func (c *Connection) To() string {
	if c.DstHost == "" {
		return c.DstIP.String()
	}
	return c.DstHost
}

func (c *Connection) String() string {
	if c.Entry == nil {
		return fmt.Sprintf("%s ->(%s)-> %s:%d", c.SrcIP, c.Protocol, c.To(), c.DstPort)
	}
	if c.Process == nil {
		return fmt.Sprintf("%s (uid:%d) ->(%s)-> %s:%d", c.SrcIP, c.Entry.UserId, c.Protocol, c.To(), c.DstPort)
	}
	return fmt.Sprintf("%s (%d) -> %s:%d (proto:%s uid:%d)", c.Process.Path, c.Process.ID, c.To(), c.DstPort, c.Protocol, c.Entry.UserId)
}