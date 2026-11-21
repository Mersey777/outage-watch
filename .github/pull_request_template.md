## Story
Closes #__ <!-- when this PR finishes the story -->
Part of #__ <!-- when the story needs more PRs; delete the line you don't use.
Use the GitHub issue number, not the OW id: OW-1 to OW-21 are #1 to #21, OW-22 is #23 -->

## What changed
<!-- 1 to 3 bullets: what a reviewer will see in the diff. -->

## Why
<!-- The problem this solves for the L1 shift or the team. -->

## How it was tested
<!-- Commands you ran and their result. -->
- [ ] `flake8 .` is clean
- [ ] `pytest` passes locally (__ passed)
- [ ] New or updated tests: <!-- e.g. TC-03, or "none: docs only" -->

## Evidence
<!-- Screenshot or pasted output for UI, CLI or pipeline changes.
Label fixture output as "fixture". Never paste a token or a room ID. -->

## Definition of Done
- [ ] GitHub Actions **test** check is green
- [ ] One approving review with a real comment
- [ ] After merge: the Jenkins build for the merge is green (tests in the JUnit report)
- [ ] After merge: Webex received the deploy announcement
- [ ] README or docs updated if users are affected
- [ ] Squash-merge title keeps the story ID, e.g. `(OW-8)`

## Reviewer focus
<!-- Optional: what you want the reviewer to look at closely. -->
