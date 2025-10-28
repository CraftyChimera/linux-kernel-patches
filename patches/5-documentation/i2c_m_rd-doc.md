### Patch Info

| Property | Value |
|-------|--------|
| **status** | Accepted |
| **patch_commit** | c3ff7f06c787 ("i2c: Clarify behavior of I2C_M_RD flag") |
| **subsystem** | I2C |
| **title** | i2c: Clarify behavior of I2C_M_RD flag |
| **discussion_url** | https://lore.kernel.org/all/20250709151402.7811-2-viswanathiyyappan@gmail.com/ |

### Summary

This patch clarifies that setting `I2C_M_RD` indicates a read transaction,
while not setting it implies a write operation.