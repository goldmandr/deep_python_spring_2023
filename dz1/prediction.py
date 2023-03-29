class SomeModel:
    def predict(self, message: str) -> float:
        return 1


def predict_message_mood(
    message: str,
    model: SomeModel,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    if model < bad_thresholds:
        return "неуд"
    elif model > good_thresholds:
        return "отл"
    else:
        return "норм"
