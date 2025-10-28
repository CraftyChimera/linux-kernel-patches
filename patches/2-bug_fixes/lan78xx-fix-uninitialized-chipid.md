### Patch Info

| Property | Value |
|-------|--------|
| **status** | Accepted|
| **patch_commit** | 8d93ff40d49d ("net: usb: lan78xx: fix use of improperly initialized dev->chipid in lan78xx_reset")  |
| **regression_commit** | a0db7d10b76e ("lan78xx: Add to handle mux control per chip id") |
| **subsystem** | net |
| **title** | net: usb: lan78xx: fix use of improperly initialized dev->chipid in lan78xx_reset |
| **dashboard_url** | not from syzkaller |
| **discussion_url** | https://patch.msgid.link/20251013181648.35153-1-viswanathiyyappan@gmail.com |
| **backported** | yes |

### Summary

`dev->chipid` was being used in `lan78xx_init_mac_address()` before it was initialized.

This patch fixes the initialization order by setting `dev->chipid` before calling `lan78xx_init_mac_address()`.

I discovered this issue while investigating a [Syzkaller-reported bug](https://syzkaller.appspot.com/bug?extid=62ec8226f01cb4ca19d9).