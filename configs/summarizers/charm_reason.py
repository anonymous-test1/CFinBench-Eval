from mmengine.config import reasond_base

with reasond_base():
    from .groups.charm_reason import charm_reason_summary_groups

summarizer = dict(
    dataset_abbrs=[
        'charm-reason-Direct',
        'charm-reason-ZH-CoT',
        'charm-reason-EN-CoT',
        'charm-reason-XLT',
        'charm-reason-Translate-EN',
        '',
        'charm-reason-Chinese_Direct',
        'charm-reason-Chinese_ZH-CoT',
        'charm-reason-Chinese_EN-CoT',
        'charm-reason-Chinese_XLT',
        'charm-reason-Chinese_Translate-EN',
        'charm-reason-Global_Direct',
        'charm-reason-Global_ZH-CoT',
        'charm-reason-Global_EN-CoT',
        'charm-reason-Global_XLT',
        'charm-reason-Global_Translate-EN',
        '',
        'charm-reason-Chinese_Anachronisms_Judgment_Direct',
        'charm-reason-Chinese_Movie_and_Music_Recommendation_Direct',
        'charm-reason-Chinese_Natural_Language_Inference_Direct',
        'charm-reason-Chinese_Reading_Comprehension_Direct',
        'charm-reason-Chinese_Sequence_Understanding_Direct',
        'charm-reason-Chinese_Sport_Understanding_Direct',
        'charm-reason-Chinese_Time_Understanding_Direct',
        'charm-reason-Global_Anachronisms_Judgment_Direct',
        'charm-reason-Global_Movie_and_Music_Recommendation_Direct',
        'charm-reason-Global_Natural_Language_Inference_Direct',
        'charm-reason-Global_Reading_Comprehension_Direct',
        'charm-reason-Global_Sequence_Understanding_Direct',
        'charm-reason-Global_Sport_Understanding_Direct',
        'charm-reason-Global_Time_Understanding_Direct',
        'charm-reason-Chinese_Anachronisms_Judgment_ZH-CoT',
        'charm-reason-Chinese_Movie_and_Music_Recommendation_ZH-CoT',
        'charm-reason-Chinese_Natural_Language_Inference_ZH-CoT',
        'charm-reason-Chinese_Reading_Comprehension_ZH-CoT',
        'charm-reason-Chinese_Sequence_Understanding_ZH-CoT',
        'charm-reason-Chinese_Sport_Understanding_ZH-CoT',
        'charm-reason-Chinese_Time_Understanding_ZH-CoT',
        'charm-reason-Global_Anachronisms_Judgment_ZH-CoT',
        'charm-reason-Global_Movie_and_Music_Recommendation_ZH-CoT',
        'charm-reason-Global_Natural_Language_Inference_ZH-CoT',
        'charm-reason-Global_Reading_Comprehension_ZH-CoT',
        'charm-reason-Global_Sequence_Understanding_ZH-CoT',
        'charm-reason-Global_Sport_Understanding_ZH-CoT',
        'charm-reason-Global_Time_Understanding_ZH-CoT',
        'charm-reason-Chinese_Anachronisms_Judgment_EN-CoT',
        'charm-reason-Chinese_Movie_and_Music_Recommendation_EN-CoT',
        'charm-reason-Chinese_Natural_Language_Inference_EN-CoT',
        'charm-reason-Chinese_Reading_Comprehension_EN-CoT',
        'charm-reason-Chinese_Sequence_Understanding_EN-CoT',
        'charm-reason-Chinese_Sport_Understanding_EN-CoT',
        'charm-reason-Chinese_Time_Understanding_EN-CoT',
        'charm-reason-Global_Anachronisms_Judgment_EN-CoT',
        'charm-reason-Global_Movie_and_Music_Recommendation_EN-CoT',
        'charm-reason-Global_Natural_Language_Inference_EN-CoT',
        'charm-reason-Global_Reading_Comprehension_EN-CoT',
        'charm-reason-Global_Sequence_Understanding_EN-CoT',
        'charm-reason-Global_Sport_Understanding_EN-CoT',
        'charm-reason-Global_Time_Understanding_EN-CoT',
        'charm-reason-Chinese_Anachronisms_Judgment_XLT',
        'charm-reason-Chinese_Movie_and_Music_Recommendation_XLT',
        'charm-reason-Chinese_Natural_Language_Inference_XLT',
        'charm-reason-Chinese_Reading_Comprehension_XLT',
        'charm-reason-Chinese_Sequence_Understanding_XLT',
        'charm-reason-Chinese_Sport_Understanding_XLT',
        'charm-reason-Chinese_Time_Understanding_XLT',
        'charm-reason-Global_Anachronisms_Judgment_XLT',
        'charm-reason-Global_Movie_and_Music_Recommendation_XLT',
        'charm-reason-Global_Natural_Language_Inference_XLT',
        'charm-reason-Global_Reading_Comprehension_XLT',
        'charm-reason-Global_Sequence_Understanding_XLT',
        'charm-reason-Global_Sport_Understanding_XLT',
        'charm-reason-Global_Time_Understanding_XLT',
        'charm-reason-Chinese_Anachronisms_Judgment_Translate-EN',
        'charm-reason-Chinese_Movie_and_Music_Recommendation_Translate-EN',
        'charm-reason-Chinese_Natural_Language_Inference_Translate-EN',
        'charm-reason-Chinese_Reading_Comprehension_Translate-EN',
        'charm-reason-Chinese_Sequence_Understanding_Translate-EN',
        'charm-reason-Chinese_Sport_Understanding_Translate-EN',
        'charm-reason-Chinese_Time_Understanding_Translate-EN',
        'charm-reason-Global_Anachronisms_Judgment_Translate-EN',
        'charm-reason-Global_Movie_and_Music_Recommendation_Translate-EN',
        'charm-reason-Global_Natural_Language_Inference_Translate-EN',
        'charm-reason-Global_Reading_Comprehension_Translate-EN',
        'charm-reason-Global_Sequence_Understanding_Translate-EN',
        'charm-reason-Global_Sport_Understanding_Translate-EN',
        'charm-reason-Global_Time_Understanding_Translate-EN',
    ],
    summary_groups=sum(
        [v for k, v in locals().items() if k.endswith('_summary_groups')], [])
)
