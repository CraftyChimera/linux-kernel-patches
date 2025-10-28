# Patches Directory

This directory contains Linux kernel patches I’ve worked on, organized by category (features, bug fixes, etc).

## Statistics:

### Subsystem Summary

Here's the count of upstreamed patches grouped by subsystem:

| Subsystem | Count |
| --------- | ----- |
| net       | 3     |
| mm        | 1     |
| i2c       | 2     |

### Category Summary 

| Rank | Category | Description | Count |
|------|------|-------------| ----- |
| 1 | **features** | New features and major architectural improvements | 0 |
| 2 | **bug_fixes** | Fixes for runtime bugs or crashes authored by me (often found via syzkaller) | 3 |
| 3 | **backports** | Fixes authored by others, cherry-picked from newer kernels | 0 |
| 4 | **build_fixes** | Fixes for build failures or errors specific to certain features | 0 |
| 5 | **documentation** | Improvements or Additions to documentation | 1 |
| 6 | **warn_fixes** | Fixes for compiler warnings generated during build | 0 |
| 7 | **refactor** | Code cleanups or replacements of deprecated APIs | 2 |
| 8 | **misc** | Miscellaneous patches | 0 |

## Patch Note Guidelines

Each patch note file includes a **Patch Info** table and a **Summary** section.

### Properties

- **status** — The current state of the patch (`Under Review`, `Accepted`, `Rejected`, `RFC`).
- **fix_commit** — If Accepted, this is the commit hash of the applied patch and left empty otherwise. **Applicable only to bug fix patches**
- **regression_commit** — The commit that introduced the regression. **Applicable only to bug fix patches**
- **subsystem** — The affected Kernel subsystem (e.g., `net`, `mm`, `i2c`, `usb`).
- **dashboard_url** — Link to the syzkaller dashboard. **Filled only if the bug originated from syzkaller**.
- **discussion_url** — Link to the mailing list discussion of the current version of the patch. **May be omitted for minor patches**
- **backported** — `yes/no` and, if `yes`, this is all the valid backport targets unless explicitly specified otherwise. **Applicable only to bug fix patches**

## 📁 Directory Structure

```text
patches/
├── 1-features/
│   ├── patch1.md
│   ├── patch2.md
│   ├── patch3.md
│   └── series-foo_feature/
│       ├── patch1.md
│       ├── patch2.md
│       └── README.md
├── 2-bug_fixes/
│   ├── patch1.md
│   └── patch2.md
├── 3-backports/
│   └── patch1.md
├── 4-build_fixes/
├── 5-documentation/
├── 6-warn_fixes/
├── 7-refactor/
├── 8-misc/
└── README.md
```

Individual patches are described by a single .md file while patch series get their own directory.

series-foo_feature contains patches that implement the series-foo feature which may or may not be under
the same series.