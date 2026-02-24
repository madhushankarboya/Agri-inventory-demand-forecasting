def translate(text, lang):

    # ===============================
    # COMPLETE TRANSLATION DICTIONARY
    # ===============================

    translations = {

        # ================= ENGLISH =================
        "en": {

            # Navbar
            "Dashboard": "Dashboard",
            "Forecasting": "Forecasting",
            "Inventory": "Inventory",
            "Language": "Language",
            "Login": "Login",
            "Logout": "Logout",
            "Admin": "Admin",

            # Government Header
            "Government of India": "Government of India",
            "Ministry of Agriculture & Farmers Welfare":
                "Ministry of Agriculture & Farmers Welfare",
            "National Agri AI Portal": "National Agri AI Portal",

            # Dashboard
            "National Agricultural Dashboard":
                "National Agricultural Dashboard",
            "Total States": "Total States",
            "Total Production": "Total Production",
            "Production Trend": "Production Trend",
            "Crop Comparison": "Crop Comparison",
            "Growth %": "Growth %",
            "Risk Overview": "Risk Overview",
            "Forecast Snapshot": "Forecast Snapshot",

            # Chatbot
            "AgriBot Assistant": "AgriBot Assistant",
            "Admin Mode": "Admin Mode",
            "Farmer Mode": "Farmer Mode",
            "Ask something...": "Ask something...",
            "Send": "Send",

            # Inventory
            "Government Inventory Optimization":
                "Government Inventory Optimization",
            "Select State": "Select State",
            "Select Crop": "Select Crop",
            "Calculate Inventory": "Calculate Inventory",
            "Safety Stock": "Safety Stock",
            "Reorder Point": "Reorder Point",
            "EOQ": "EOQ",
            "Risk Level": "Risk Level",
            "Download Official Government PDF":
                "Download Official Government PDF",

            # Risk
            "LOW": "LOW",
            "MEDIUM": "MEDIUM",
            "HIGH": "HIGH",
            "NO DATA": "NO DATA",

            # Forecast
            "Generate Forecast": "Generate Forecast",
            "Rainfall Change (%)": "Rainfall Change (%)",
            "Temperature Change (°C)": "Temperature Change (°C)",

            # PDF
            "Official Inventory Optimization Report":
                "Official Inventory Optimization Report",
            "State Name": "State Name",
            "Crop Name": "Crop Name",
            "Scan for Verification": "Scan for Verification",

            # Footer
            "National Informatics Centre":
                "National Informatics Centre",
            "Loading Government Portal...":
                "Loading Government Portal..."
        },

        # ================= HINDI =================
        "hi": {

            "Dashboard": "डैशबोर्ड",
            "Forecasting": "पूर्वानुमान",
            "Inventory": "इन्वेंटरी",
            "Language": "भाषा",
            "Login": "लॉगिन",
            "Logout": "लॉगआउट",
            "Admin": "प्रशासक",

            "Government of India": "भारत सरकार",
            "Ministry of Agriculture & Farmers Welfare":
                "कृषि एवं किसान कल्याण मंत्रालय",
            "National Agri AI Portal":
                "राष्ट्रीय कृषि एआई पोर्टल",

            "National Agricultural Dashboard":
                "राष्ट्रीय कृषि डैशबोर्ड",
            "Total States": "कुल राज्य",
            "Total Production": "कुल उत्पादन",
            "Production Trend": "उत्पादन प्रवृत्ति",
            "Crop Comparison": "फसल तुलना",
            "Growth %": "वृद्धि %",
            "Risk Overview": "जोखिम अवलोकन",
            "Forecast Snapshot": "पूर्वानुमान सारांश",

            "AgriBot Assistant": "एग्रीबॉट सहायक",
            "Admin Mode": "प्रशासक मोड",
            "Farmer Mode": "किसान मोड",
            "Ask something...": "कुछ पूछें...",
            "Send": "भेजें",

            "Government Inventory Optimization":
                "सरकारी इन्वेंटरी अनुकूलन",
            "Select State": "राज्य चुनें",
            "Select Crop": "फसल चुनें",
            "Calculate Inventory": "इन्वेंटरी गणना करें",
            "Safety Stock": "सुरक्षा स्टॉक",
            "Reorder Point": "पुनः आदेश बिंदु",
            "EOQ": "आर्थिक आदेश मात्रा",
            "Risk Level": "जोखिम स्तर",
            "Download Official Government PDF":
                "सरकारी पीडीएफ डाउनलोड करें",

            "LOW": "कम",
            "MEDIUM": "मध्यम",
            "HIGH": "उच्च",
            "NO DATA": "कोई डेटा नहीं",

            "Generate Forecast": "पूर्वानुमान तैयार करें",
            "Rainfall Change (%)": "वर्षा परिवर्तन (%)",
            "Temperature Change (°C)": "तापमान परिवर्तन (°C)",

            "Official Inventory Optimization Report":
                "आधिकारिक इन्वेंटरी रिपोर्ट",
            "State Name": "राज्य नाम",
            "Crop Name": "फसल नाम",
            "Scan for Verification": "सत्यापन के लिए स्कैन करें",

            "National Informatics Centre":
                "राष्ट्रीय सूचना विज्ञान केंद्र",
            "Loading Government Portal...":
                "सरकारी पोर्टल लोड हो रहा है..."
        },

        # ================= TELUGU =================
        "te": {

            "Dashboard": "డాష్‌బోర్డ్",
            "Forecasting": "అంచనా",
            "Inventory": "ఇన్వెంటరీ",
            "Language": "భాష",
            "Login": "లాగిన్",
            "Logout": "లాగౌట్",
            "Admin": "అడ్మిన్",

            "Government of India": "భారత ప్రభుత్వం",
            "Ministry of Agriculture & Farmers Welfare":
                "వ్యవసాయ మరియు రైతు సంక్షేమ మంత్రిత్వ శాఖ",
            "National Agri AI Portal":
                "జాతీయ వ్యవసాయ ఏఐ పోర్టల్",

            "National Agricultural Dashboard":
                "జాతీయ వ్యవసాయ డాష్‌బోర్డ్",
            "Total States": "మొత్తం రాష్ట్రాలు",
            "Total Production": "మొత్తం ఉత్పత్తి",
            "Production Trend": "ఉత్పత్తి ధోరణి",
            "Crop Comparison": "పంట పోలిక",
            "Growth %": "వృద్ధి %",
            "Risk Overview": "ప్రమాద స్థితి",
            "Forecast Snapshot": "అంచనా సారాంశం",

            "AgriBot Assistant": "అగ్రిబాట్ సహాయకుడు",
            "Admin Mode": "అడ్మిన్ మోడ్",
            "Farmer Mode": "రైతు మోడ్",
            "Ask something...": "ఏదైనా అడగండి...",
            "Send": "పంపండి",

            "Government Inventory Optimization":
                "ప్రభుత్వ ఇన్వెంటరీ ఆప్టిమైజేషన్",
            "Select State": "రాష్ట్రాన్ని ఎంచుకోండి",
            "Select Crop": "పంటను ఎంచుకోండి",
            "Calculate Inventory": "ఇన్వెంటరీ లెక్కించండి",
            "Safety Stock": "సేఫ్టీ స్టాక్",
            "Reorder Point": "రీఆర్డర్ పాయింట్",
            "EOQ": "ఆర్థిక ఆర్డర్ పరిమాణం",
            "Risk Level": "ప్రమాద స్థాయి",
            "Download Official Government PDF":
                "ప్రభుత్వ PDF డౌన్‌లోడ్",

            "LOW": "తక్కువ",
            "MEDIUM": "మధ్యస్థ",
            "HIGH": "అధిక",
            "NO DATA": "డేటా లేదు",

            "Generate Forecast": "అంచనా సృష్టించండి",
            "Rainfall Change (%)": "వర్షపాతం మార్పు (%)",
            "Temperature Change (°C)": "ఉష్ణోగ్రత మార్పు (°C)",

            "Official Inventory Optimization Report":
                "అధికారిక ఇన్వెంటరీ నివేదిక",
            "State Name": "రాష్ట్రం",
            "Crop Name": "పంట పేరు",
            "Scan for Verification": "ధృవీకరణ కోసం స్కాన్ చేయండి",

            "National Informatics Centre":
                "జాతీయ సమాచార కేంద్రం",
            "Loading Government Portal...":
                "ప్రభుత్వ పోర్టల్ లోడ్ అవుతోంది..."
        }
    }

    if lang in translations and text in translations[lang]:
        return translations[lang][text]

    return text