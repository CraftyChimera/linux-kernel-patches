### Patch Info

| Property | Value |
|-------|--------|
| **status** | Accepted |
| **patch_commit** | 59ccb8176bd7 ("i2c: mux: Simplify boolean assignment in i2c_mux_alloc") |
| **subsystem** | I2C |
| **title** | i2c: mux: Simplify boolean assignment in i2c_mux_alloc |
| **discussion_url** | https://lore.kernel.org/all/20250825031430.3001-1-viswanathiyyappan@gmail.com/ |

### Summary

This patch simplifies boolean assignments of the form `if (a) b = true;`
into the more compact expression `b = !!a;`