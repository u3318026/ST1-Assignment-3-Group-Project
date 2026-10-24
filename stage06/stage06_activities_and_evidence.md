# Stage 6 activities and evidence

Complete this one group record. Link actual issues, diffs, tests and reviews; avoid copying entire histories. Blank fields are intentional. Duplicate rows as needed. Use synthetic data only. Every member records their own meaningful contribution. Do not invent results, reviews or Copilot use.

- Group/tutorial: Group 6 Wednesday 2:30-4:30pm
- Members, GitHub usernames and cohorts: Tamas Szucs = github username = u3318026 = Undergraduate, Ryan Grieves github username = BlackJack2180and Undergraduate, Md Tahmid Ul Islam Tonmoy github username = tahmidtonmoy and Postgraduate
- Repository URL: https://github.com/u3318026/ST1-Assignment-3-Group-Project
- Starting SHA: a4933c1e1f7a40ec38a22d9c9b48fe7493e41ef5

## A Requirement to issue activities

### FR-02 Patient Search

- Title: [response]
- Context: [response]
- Requirement: [response]
- Acceptance criteria: [response]
- Scope: [response]
- Definition of Done: [response]
- Owner: [response]
- Actual issue link: [response]

### FR-06 Appointment Cancellation with FR-07 retained history

- Title: [response]
- Context: [response]
- Requirement: [response]
- Acceptance criteria: [response]
- Scope: [response]
- Definition of Done: [response]
- Owner: [response]
- Actual issue link: [response]

## B Commit quality

| Original example | Strong or Weak | Reason |
|---|---|---|
| changes | [select] | [response] |
| final version | [select] | [response] |
| Add patient search by ID | [select] | [response] |
| fix stuff | [select] | [response] |
| Prevent cancellation of completed appointments | [select] | [response] |

## C Over scoped PR review

A cancellation PR also renames unrelated patient fields, restructures unrelated code and adds a new dependency.

- Scope concerns: [response]
- Responsibility and architecture concerns: [response]
- Testing and review concerns: [response]
- Changes to remove or separate, with reasons: [response]

## D Challenge a weak Copilot review

GitHub Copilot says: "Looks good; tests pass."

- Missing evidence: [response]
- Follow-up review question 1: [response]
- Follow-up review question 2: [response]
- Follow-up review question 3: [response]
- Follow-up review question 4: [response]
- Follow-up review question 5: [response]
- Additional questions if useful: [response]

## E Team workflow agreement

| Practice | Team agreement |
|---|---|
| Branch naming | [response] |
| Commit message convention | [response] |
| PR size | [response] |
| Another-member review requirement | [response] |
| Merge rule | [response] |
| Significant Copilot disclosure rule | [response] |

## F Issue and backlog index

Create at least two focused issues. Add a linked practitioner-lookup issue or an explicit supporting criterion with the tutor if needed to cover all three service targets.

| Issue link | Requirement | Owner | Acceptance criteria or precise link | Status |
|---|---|---|---|---|
| [issue 1] | [response] | [response] | [response] | [response] |
| [issue 2] | [response] | [response] | [response] | [response] |

## G Pull request evidence

Repeat this block per PR. Record actual events, not planned approvals.

- PR link and title: [response]
- Linked issue and requirement: [response]
- Feature branch: [response]
- Changed behaviour: [response]
- Meaningful commits: [links]
- Test command, directory and observed result: [response]
- Another-member reviewer: [response]
- Human observations recorded before Copilot: [link and time]
- Requirement, responsibilities, test assertions and unrelated-scope checks: [response]
- Key feedback: [response]
- Author response/change and verification: [response]
- Reviewer recheck and approval: [link]
- Merge outcome and SHA: [response]
- Significant Copilot assistance: [summary or none]
- Linked issue closure: [response]
- Each member updated main: [member and confirmation]
- Integrated verification after merge: [command, directory, result and code SHA]

## H Copilot collaboration record

Record meaningful required use, not every trivial completion. Repeat per significant interaction.

- Member and task: [response]
- Prompt/purpose and relevant issue/diff: [response]
- Summary of output: [response]
- Human check against actual code, requirements and tests: [response]
- Decision — Accept / Modify / Reject: [select]
- Reason: [response]
- Verification/evidence: [link and result]

## I Human versus Copilot review comparison

- Human reviewer noticed before consulting Copilot: [response]
- Copilot noticed: [response]
- Overlap: [response]
- What did the human reviewer notice that Copilot did not: [response]
- What did Copilot identify that the human reviewer initially missed: [response]
- Unsupported or incorrect Copilot suggestion: [response or none identified with explanation]
- Human judgement accepted, modified or rejected, and why: [response]
- Which evidence justified merge approval: [response]

## J Contributions

Repeat per member. Include only categories that describe actual work; write not applicable where appropriate. Pairing or mentoring can be supported by a short corroborated note.

- Member: [response]
- Implementation: [work and evidence]
- Testing: [work and evidence]
- Review: [work and evidence]
- Issue refinement: [work and evidence]
- Design and responsibility discussion: [work and evidence]
- Debugging or integration: [work and evidence]
- Documentation or team support: [work and evidence]

## K Exit question

Why is a high commit count not necessarily evidence of strong contribution?

Answer: A high commit count doesnt give evidence of strong contribution because the quality of those commits might be very poor. So although on paper it lloks like they are contributing heaps, they could just be changing one small thing, committing and making it look like they are doing heaps of work when they actually arent. You can commit anything after even typing one character, so its not about the quanitity of the commits but raather the quality.

## L Stage 6 formative questions

1. What is version control?

Version control is a way of tracking and controlling differnt changes to a document or file over time.

2. Why is a feature branch useful?

It is useful because we can beuild specific things outside of the main branch, which means that we can do more testingt and enhancing without the fear of braking saomething on the main file.

3. What makes a commit a good engineering commit?

A good engineering commit is when it is clearly documented, focuses on purely one task at a time, and make sure that explanations of changes are easy to understand, so future users can understan and if you need to traceback, you can understand as well.

4. What is a pull request?

A pull request is when you divert from the main branch and work on that, and then when you finish you want to merge your work back onto the main branch, which is defined as the pull request.

5. What is the purpose of code review?

The prupose is to make sure that the proposed work is useful and the work doesnt interfere or break existing code. Reviewing the code before it is merged back to main makes sure that the existing code on the main and the new code isn't going to break the system.

6. What does a Git diff show?

A git diff shows the difference between a past version and the new version, The new code will have a green highlighted look, and the removed lines or code will have a red highlight, this makes it easy to see what is added and removed in between different commits.

7. What is a Definition of Done?

The definition of done is meeting the given criteria. This can be based off of quality, tehnical capabilities, but once those criteria are met, it is considered done.

8. What is the appropriate role of GitHub Copilot in pull-request review?

The approprioate use of github copilot in the pull request review is to use it as a tool for automated review, it shouldnt mean that it is the only one to review it, but it can be the first to review since it can be automated to check it as soon as you do the pull reuqest. It shouldnt be used for comprehensive and deep analysis, but a quick general overview of work and feedback.

9. Why should individual contribution not be judged only by commit count?

A persons commit count shouldnt be related to how much work they put in, if your commit quality is poor, but have a million commits, it looks like you are doing lots of work, but realistically you are arent. Quality is much more preferred over quantity.

10. What is the Stage 6 engineering rule?

The stage 6 engineering rule is to make sure that your commits are meaningful and provide quality changes, rather than sloppy commits that you make over and over, trying to increase your commit count to seem like your doing work, but you actually arent.

## M Completion and handover

- Starting SHA: [response]
- Final Stage 6 code SHA: [response]
- Test command: [response]
- Working directory: [response]
- Observed result: [response]
- PR and another-member reviewer: [links]
- Unresolved issue or none: [response]
- Stage 7 handover status: [ready for tutor checkpoint / unresolved work]
- Final submitted SHA if later than tested SHA: [response and evidence-only difference]

- [ ] Three Stage 6 service targets completed and checked.
- [ ] Original supplied tests retained and passing.
- [ ] At least two focused issues link requirements and acceptance criteria.
- [ ] Feature work reviewed by another member using the actual diff.
- [ ] Human-first review and required Copilot comparison recorded.
- [ ] Feedback resolved and approval recorded before merge.
- [ ] Everyone pulled main and integrated checks passed.
- [ ] Required activities, quiz responses and contribution notes completed.
- [ ] Only synthetic data included; confidential peer material kept out.
- [ ] Tutor can trace a requirement through issue, code, tests, PR and checkpoint.

Do not write a file's own future commit SHA into that file. Record the tested code SHA first, then commit the evidence; explain the difference when submitting.
