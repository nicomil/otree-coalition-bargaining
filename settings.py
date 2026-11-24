"""Local demo configuration for the public oTree experiment."""
import os
import secrets

SESSION_CONFIGS = [
    dict(
        name="bargaining_tdl",
        display_name="Coalition bargaining (three treatments)",
        app_sequence=["bargaining_tdl_intro", "bargaining_tdl_main", "bargaining_tdl_survey"],
        num_demo_participants=18,
        active_treatments=["private", "public", "private_no_dwl"],
    ),
]
SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.0,
    participation_fee=1.0,
    doc="Local demo with synthetic participants",
    control_questions_max_attempts=5,
    skip_intro_control_questions=False,
    use_test_timers=False,
    require_prolific_id=False,
    completionlink="",
    dropoutlink_cq="",
    dropoutlink_inactive="",
)

PARTICIPANT_FIELDS = [
    "prolific_id",
    "prolific_study_id",
    "prolific_session_id",
    "inactive_excluded",
    "inactive_excluded_reason",
    "group_dropped",
    "part1_payoff_eligible",
    "treatment",
    "allocation_slot",
    "allocation_block",
    "allocation_attempt",
    "assignment_timestamp",
    "assignment_status",
    "is_replacement",
    "allocation_failure_reason",
    "group_outcome",
    "part1_group_id",
]
SESSION_FIELDS = [
    "randomization_seed",
    "randomization_schedule",
    "randomization_block_size",
]
LANGUAGE_CODE = "en"
REAL_WORLD_CURRENCY_CODE = "USD"
USE_POINTS = False
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = os.environ.get("OTREE_ADMIN_PASSWORD")
SECRET_KEY = os.environ.get("OTREE_SECRET_KEY") or secrets.token_urlsafe(32)
INSTALLED_APPS = ["otree"]
