def get_result_content(risk_level):

    if risk_level == "Low Risk":
        return {
            "greeting": "🎉 Congratulations!",
            "message": "Your mental wellbeing appears healthy and balanced.",
            "image": "low_risk.jpg",
            "video": "https://www.youtube.com/embed/ZToicYcHIOU",
            "suggestions": [
                "Maintain your healthy routine",
                "Stay socially active",
                "Practice gratitude daily",
                "Continue physical activities you enjoy"
            ]
        }

    elif risk_level == "Moderate Risk":
        return {
            "greeting": "⚠️ Gentle Alert",
            "message": "Some early signs of stress are visible. Small changes can help.",
            "image": "moderate_risk.png",
            "video": "https://www.youtube.com/embed/inpok4MKVLM",
            "suggestions": [
                "Start light exercise like walking or yoga",
                "Improve sleep routine",
                "Reduce screen time",
                "Talk openly with friends or family"
            ]
        }

    else:
        return {
            "greeting": "🚨 Attention Needed",
            "message": "High stress indicators detected. Support and care are important.",
            "image": "High_risk.jpg",
            "video": "https://www.youtube.com/embed/tybOi4hjZFQ",
            "suggestions": [
                "Practice daily stress-relief exercises",
                "Avoid isolation and stay connected",
                "Reduce workload and take breaks",
                "Consider professional mental health support"
            ]
        }
