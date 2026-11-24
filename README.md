# oTree coalition bargaining

How do public and private conversations shape coalition formation? Three players exchange messages and decide whom to support. The experiment compares private communication, public communication, and private communication with a different payoff rule when players fail to reach an agreement.

## Run a local session

Use Python 3.11. From the repository root on macOS or Linux:

```sh
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt requests
otree test bargaining_tdl 18
```

The bot test simulates 18 participants and exercises the three treatments. To explore the screens manually, run `otree devserver`, open the local URL printed by oTree, and select **Coalition bargaining (three treatments)**. Use synthetic responses and leave recruitment identifiers empty. The demo has no study completion URLs.

## Source layout

| Directory | Purpose |
|---|---|
| `bargaining_tdl_intro/` | Instructions, comprehension checks and treatment assignment |
| `bargaining_tdl_main/` | Group formation, communication, decisions and payoffs |
| `bargaining_tdl_survey/` | Final questionnaire and results |
| `bargaining_tdl_common/` | Shared treatment rules and helpers |
