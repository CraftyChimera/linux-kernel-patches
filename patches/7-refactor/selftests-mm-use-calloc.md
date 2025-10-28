### Patch Info

| Property | Value |
|-------|--------|
| **status** | Accepted |
| **patch_commit** | 79dfed097680 ("selftests/mm: use calloc instead of malloc in pagemap_ioctl.c") |
| **subsystem** | mm |
| **title** | selftests/mm: use calloc instead of malloc in pagemap_ioctl.c |
| **discussion_url** | https://lkml.kernel.org/r/20250825170643.63174-1-viswanathiyyappan@gmail.com |

### Summary

This patch replaces `malloc` with `calloc` in the mm selftest `pagemap_ioctl.c`, ensuring buffers are zero-initialized and preventing potential use of uninitialized memory.