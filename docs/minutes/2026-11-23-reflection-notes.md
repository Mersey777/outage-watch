# Activity 4 reflection notes

| | |
|---|---|
| **Date** | Mon Nov 23, 2026 |
| **Collected by** | Chylle Frias |
| **Answers from** | Matthew Magtoto, Asher Sta. Ana, Shane Cruz, Chylle Frias |
| **Used for** | The team reflection in the Activity 4 submission (briefing, Section 11) |

Each member's written answer, summarised. The briefing planned this file as
`2026-11-22-reflection-notes.md`; the answers were written on Nov 23, so the file uses that date.

## Matthew Magtoto (Scrum Leader, API Integration Specialist)

- **Worked well:** clear roles, and the merge gate worked.
- **Team problem:** a dependent two-day schedule with him as the only repo admin. Handled
  with a written plan and Webex stand-ups.
- **Technical problem:** his CI gate blocked the first PRs because it tested files not merged
  yet. Fixed in #22.
- **Accountability:** one owner per story; no admin bypass of the gate.
- **Decisions:** options are posted in Webex, the owner of the area decides, and the decision
  goes in the minutes.
- **Lesson:** test the gate with a real PR before locking `main`.

## Asher Sta. Ana (Lead Python Developer, CI/CD Engineer)

- **Worked well:** peer review caught real issues (#25, #26).
- **Team problem:** his Jenkins PR (#28) waited about two hours for review; Shane unblocked it.
- **Technical problem:** the VM's Docker was too old for the planned image. He ran the stock
  Jenkins image with relaxed security, installed Python, fixed the plugins and added SCM
  polling.
- **Schedule:** recording moved to Monday.
- **Lesson:** test the real environment early.

## Shane Cruz (QA/Testing Engineer)

- **Worked well:** the role split made CI verification automatic.
- **Team problem:** the demo hand-offs overlapped. Fixed with a step-by-step script.
- **Technical problem:** failure states needed testing without live outages. Covered with
  fixtures and `mock.patch`.
- **Accountability:** branch protection held his deliberate TC-07 bug until it was fixed.
- **Lesson:** a gate is only as good as its edge cases.

## Chylle Frias (Recorder and UI Designer)

- **Worked well:** the role split, and Asher's review of the PR template.
- **Team problem:** the 9:00 AM kickoff was missed; the team caught up at 8:00 PM, and the
  kickoff minutes record it honestly.
- **Process problem:** the template PR (#25) merged before the minutes were in, so a follow-up
  PR (#26) was needed, which also fixed the "Closes # / Part of #" hint.
- **Accountability:** owned the minutes and the evidence folder.
- **Decisions recorded:** moving the submission to Monday; recording the demo in one session.
- **Lesson:** write things down as they happen, and keep them honest.
