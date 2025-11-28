### Patch Info

| Property | Value |
|-------|--------|
| **status** | Accepted |
| **patch_commit** | 958baf5eaee3 ("net: usb: Remove disruptive netif_wake_queue in rtl8150_set_multicast") |
| **regression_commit** | 1da177e4c3f4 ("Linux-2.6.12-rc2") |
| **subsystem** | net |
| **title** | net: usb: Remove disruptive netif_wake_queue in rtl8150_set_multicast |
| **dashboard_url** | https://syzkaller.appspot.com/bug?extid=78cae3f37c62ad092caa |
| **discussion_url** | https://patch.msgid.link/20250924134350.264597-1-viswanathiyyappan@gmail.com |
| **backported** | yes |
| **blog_url** | https://craftychimera.github.io/posts/linux/syzkaller/ |

### Summary

syzbot reported [WARNING in rtl8150_start_xmit/usb_submit_urb](https://syzkaller.appspot.com/bug?extid=78cae3f37c62ad092caa).

This happened because of the following sequence of events:

```c
    rtl8150_start_xmit() {
            netif_stop_queue();
            usb_submit_urb(dev->tx_urb);
    }
    
    rtl8150_set_multicast() {
            netif_stop_queue();
            netif_wake_queue();             // wakes up TX queue before URB is done
    }
    
    rtl8150_start_xmit() {
            netif_stop_queue();
            usb_submit_urb(dev->tx_urb);    // double submission
    }
```

`rtl8150_set_multicast()` should not be concerned with TX queue synchronization, as it's a ndo_set_rx_mode callback.

This patch removes these disruptive queue control calls and prevents the double USB URB submission bug.