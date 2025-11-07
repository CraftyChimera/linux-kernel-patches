### Patch Info

| Property | Value |
|-------|--------|
| **status** | Ongoing |
| **patch_commit** | |
| **subsystem** | net  |
| **title** | net: Split ndo_set_rx_mode into snapshot and deferred write |
| **discussion_url** | https://lore.kernel.org/netdev/20251028174222.1739954-1-viswanathiyyappan@gmail.com/ |

### Summary

set_rx_mode is problematic because of it's inability to sleep. 

There are drivers that avoid this by having the meat of set_rx_mode done in a work item but that is extra work that can be avoided if we standardize this in core.

Therefore, this series provides that standardization by splitting set_rx_mode into rx_config snapshot and deferred write;

set_rx_mode will be responsible for capturing all the relevant data in rx_config at the time of its call and write_rx_config will be responsible for writing that captured data onto the hardware