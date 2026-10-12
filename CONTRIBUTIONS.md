# Open-source review practice

I use AI tools to help inspect unfamiliar code, then frame findings as specific risks and questions that maintainers can investigate. These entries document reports and analysis, not merged fixes or confirmed production incidents.

## Open Code Review

### Quoted filenames disappearing from diff review

A report about Git-quoted paths, such as filenames containing a tab, failing to match the diff parser's file-header rule. The changed file can then disappear from the review input. The product question is whether a user can distinguish “no findings” from “not reviewed.”

[Issue #1492](https://github.com/alibaba/open-code-review/issues/1492)

### Filename handling during repository scans

A report about trimming leading or trailing whitespace from valid filenames returned by a NUL-delimited Git listing. That changes the path before a filesystem lookup and can skip the real tracked file. The product concern is silent omission: the scan appears complete while its coverage may be incomplete.

[Issue #1493](https://github.com/alibaba/open-code-review/issues/1493)

### Repository identity and scan recovery

A follow-up investigation connected to an existing issue about repository identity and recovery behaviour. It explores whether repeated or conflicting repository state can prevent a scan from recovering as expected.

[Follow-up on issue #894](https://github.com/alibaba/open-code-review/issues/894#issuecomment-5748485061)

## How I discuss this work

“I used AI-assisted code inspection to identify potential failure paths, connected them to user-facing risks, and submitted concrete issue reports or follow-up analysis. I distinguish a reported concern from a maintainer-confirmed defect, and an issue contribution from an implemented fix.”

For current discussion and maintainer decisions, the linked threads are the source of truth.

---

[Back to my profile](README.md)
