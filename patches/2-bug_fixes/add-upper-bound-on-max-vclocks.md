### Patch Info

| Property | Value |
|-------|--------|
| **status** | Accepted |
| **patch_commit** | e9f35294e18d ("ptp: Add a upper bound on max_vclocks")  |
| **regression_commit** | 73f37068d540 ("ptp: support ptp physical/virtual clocks conversion") |
| **subsystem** | net  |
| **title** | ptp: Add a upper bound on max_vclocks |
| **dashboard_url** | https://syzkaller.appspot.com/bug?extid=94d20db923b9f51be0df |
| **discussion_url** | https://patch.msgid.link/20250925155908.5034-1-viswanathiyyappan@gmail.com |
| **backported** | no |

### Summary

syzbot reported [WARNING in max_vclocks_store](https://syzkaller.appspot.com/bug?extid=94d20db923b9f51be0df).

This occured when the argument max is too large for kcalloc to handle.

This patch extends the guard to guard against values that are too large for kcalloc.