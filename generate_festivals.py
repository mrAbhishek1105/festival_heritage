import json
import random

# Load existing data
file_path = 'src/data/festivals.json'
with open(file_path, 'r', encoding='utf-8') as f:
    existing_data = json.load(f)

# States and base coordinates
states_data = {
    "Andhra Pradesh": {"lat": 15.9129, "lng": 79.7400},
    "Arunachal Pradesh": {"lat": 28.2180, "lng": 94.7278},
    "Assam": {"lat": 26.2006, "lng": 92.9376},
    "Bihar": {"lat": 25.0961, "lng": 85.3131},
    "Chhattisgarh": {"lat": 21.2787, "lng": 81.8661},
    "Goa": {"lat": 15.2993, "lng": 74.1240},
    "Gujarat": {"lat": 22.2587, "lng": 71.1924},
    "Haryana": {"lat": 29.0588, "lng": 76.0856},
    "Himachal Pradesh": {"lat": 31.1048, "lng": 77.1734},
    "Jharkhand": {"lat": 23.6102, "lng": 85.2799},
    "Karnataka": {"lat": 15.3173, "lng": 75.7139},
    "Kerala": {"lat": 10.8505, "lng": 76.2711},
    "Madhya Pradesh": {"lat": 22.9734, "lng": 78.6569},
    "Maharashtra": {"lat": 19.7515, "lng": 75.7139},
    "Manipur": {"lat": 24.6637, "lng": 93.9063},
    "Meghalaya": {"lat": 25.4670, "lng": 91.3662},
    "Mizoram": {"lat": 23.1645, "lng": 92.9376},
    "Nagaland": {"lat": 26.1584, "lng": 94.5624},
    "Odisha": {"lat": 20.9517, "lng": 85.0985},
    "Punjab": {"lat": 31.1471, "lng": 75.3412},
    "Rajasthan": {"lat": 27.0238, "lng": 74.2179},
    "Sikkim": {"lat": 27.5330, "lng": 88.5122},
    "Tamil Nadu": {"lat": 11.1271, "lng": 78.6569},
    "Telangana": {"lat": 18.1124, "lng": 79.0193},
    "Tripura": {"lat": 23.9408, "lng": 91.9882},
    "Uttar Pradesh": {"lat": 26.8467, "lng": 80.9462},
    "Uttarakhand": {"lat": 30.0668, "lng": 79.0193},
    "West Bengal": {"lat": 22.9868, "lng": 87.8550},
    "Jammu & Kashmir": {"lat": 33.7782, "lng": 76.5762},
    "Delhi": {"lat": 28.7041, "lng": 77.1025}
}

# 9 Templates to generate 270 festivals (9 * 30 states)
templates = [
    {
        "name_template": "Spring Harvest Festival of {state}",
        "religion": "Cultural",
        "month": "March-April",
        "startDate": "2026-03-15",
        "endDate": "2026-03-18",
        "why": "Celebrating the arrival of spring and harvest season in {state}.",
        "how": "People gather in local fairs, perform traditional dances, and share freshly harvested crops.",
        "food": "Local sweetmeats and dishes made from fresh agricultural produce native to {state}.",
        "dress": "Colorful traditional spring attire specific to {state}.",
        "ritual": "Offering first fruits and crops of the season to deities.",
        "hindi_why": "{state} में वसंत और फसल के मौसम के आगमन का जश्न।",
        "hindi_how": "लोग मेलों में इकट्ठा होते हैं, पारंपरिक नृत्य करते हैं और नई फसल बांटते हैं।",
        "hindi_food": "{state} की ताजी कृषि उपज से बनी स्थानीय मिठाइयाँ और व्यंजन।",
        "hindi_dress": "{state} के विशिष्ट रंगीन पारंपरिक वसंत परिधान।",
        "hindi_ritual": "देवताओं को मौसम के पहले फल और फसल चढ़ाना।"
    },
    {
        "name_template": "{state} Kite Mahotsav",
        "religion": "Cultural",
        "month": "January",
        "startDate": "2026-01-14",
        "endDate": "2026-01-16",
        "why": "Marking the transition of the sun into the zodiacal sign of Makara (Capricorn).",
        "how": "Locals fill the sky with vibrant kites, organizing friendly competitions across {state}.",
        "food": "Til (sesame) laddoos, jaggery sweets, and regional winter delicacies of {state}.",
        "dress": "Comfortable casual or traditional wear suited for outdoor kite flying.",
        "ritual": "Taking early morning holy dips in regional rivers if available, followed by sun worship.",
        "hindi_why": "मकर राशि में सूर्य के प्रवेश का प्रतीक है।",
        "hindi_how": "स्थानीय लोग आकाश को जीवंत पतंगों से भर देते हैं, {state} में अनुकूल प्रतियोगिताओं का आयोजन करते हैं।",
        "hindi_food": "तिल के लड्डू, गुड़ की मिठाइयां और {state} के क्षेत्रीय शीतकालीन व्यंजन।",
        "hindi_dress": "बाहर पतंग उड़ाने के लिए उपयुक्त आरामदायक आकस्मिक या पारंपरिक परिधान।",
        "hindi_ritual": "प्रातःकाल नदियों में पवित्र स्नान करना, उसके बाद सूर्य पूजा।"
    },
    {
        "name_template": "Monsoon Celebration of {state}",
        "religion": "Cultural/Folk",
        "month": "July-August",
        "startDate": "2026-07-25",
        "endDate": "2026-07-27",
        "why": "Welcoming the life-giving monsoon rains essential for agriculture in {state}.",
        "how": "Folk songs dedicating to the rain gods, swinging on decorated swings, and community feasts.",
        "food": "Fried snacks like pakoras, malpua, and traditional {state} monsoon specialties.",
        "dress": "Bright green and traditional festive wear reflecting the lush surroundings.",
        "ritual": "Prayers to Lord Indra or local rain deities for a bountiful agricultural yield.",
        "hindi_why": "{state} में कृषि के लिए आवश्यक जीवनदायिनी मानसूनी बारिश का स्वागत करना।",
        "hindi_how": "वर्षा देवताओं को समर्पित लोक गीत, सजे हुए झूलों पर झूलना और सामुदायिक दावतें।",
        "hindi_food": "पकोड़े, मालपुआ और पारंपरिक {state} मानसून की विशेषताएँ जैसे तले हुए स्नैक्स।",
        "hindi_dress": "लश पर्यावरण को दर्शाने वाले चमकीले हरे और पारंपरिक उत्सव परिधान।",
        "hindi_ritual": "प्रचुर कृषि उपज के लिए भगवान इंद्र या स्थानीय वर्षा देवताओं से प्रार्थना।"
    },
    {
        "name_template": "{state} Heritage & Arts Festival",
        "religion": "Cultural",
        "month": "November",
        "startDate": "2026-11-10",
        "endDate": "2026-11-15",
        "why": "Showcasing the rich artistic heritage, crafts, and history of {state}.",
        "how": "Art exhibitions, handicraft melas, theatrical performances, and classical music concerts.",
        "food": "A vast gastronomic village featuring authentic multi-cuisine delicacies of {state}.",
        "dress": "A mix of modern casual and extremely traditional heritage garments of {state}.",
        "ritual": "A completely secular and cultural celebration focused on art preservation.",
        "hindi_why": "{state} की समृद्ध कलात्मक विरासत, शिल्प और इतिहास का प्रदर्शन।",
        "hindi_how": "कला प्रदर्शनियां, हस्तशिल्प मेले, नाट्य प्रदर्शन और शास्त्रीय संगीत कार्यक्रम।",
        "hindi_food": "एक विशाल गैस्ट्रोनॉमिक गांव जिसमें {state} के प्रामाणिक बहु-व्यंजन व्यंजन हैं।",
        "hindi_dress": "{state} के आधुनिक आकस्मिक और अत्यंत पारंपरिक विरासत कपड़ों का मिश्रण।",
        "hindi_ritual": "कला संरक्षण पर केंद्रित एक पूरी तरह से धर्मनिरपेक्ष और सांस्कृतिक उत्सव।"
    },
    {
        "name_template": "Winter Carnival of {state}",
        "religion": "Cultural",
        "month": "December",
        "startDate": "2026-12-20",
        "endDate": "2026-12-26",
        "why": "Celebrating the winter season and promoting winter tourism in {state}.",
        "how": "Street parades, food stalls, bonfire nights, and local music performances.",
        "food": "Warm winter foods, roasted nuts, local teas, and traditional {state} sweets.",
        "dress": "Heavy woolen traditional garments to stay warm during outdoor evening events.",
        "ritual": "Community bonfires and storytelling sessions of {state} folklore.",
        "hindi_why": "{state} में सर्दियों के मौसम का जश्न मनाना और शीतकालीन पर्यटन को बढ़ावा देना।",
        "hindi_how": "सड़क परेड, फूड स्टॉल, अलाव की रातें और स्थानीय संगीत प्रदर्शन।",
        "hindi_food": "गर्म सर्दियों के खाद्य पदार्थ, भूने हुए मेवे, स्थानीय चाय और पारंपरिक {state} की मिठाइयाँ।",
        "hindi_dress": "बाहरी शाम के कार्यक्रमों के दौरान गर्म रहने के लिए भारी ऊनी पारंपरिक कपड़े।",
        "hindi_ritual": "सामुदायिक अलाव और {state} के लोककथाओं के कहानी सुनाने वाले सत्र।"
    },
    {
        "name_template": "Navratri Utsav {state}",
        "religion": "Hindu",
        "month": "October",
        "startDate": "2026-10-10",
        "endDate": "2026-10-19",
        "why": "Nine nights dedicating to the nine forms of Goddess Durga across {state}.",
        "how": "Community dances (like Garba/Dandiya), fasting, and elaborate pandal hopping.",
        "food": "Strictly vegetarian, fasting foods (Vrat food) like Sabudana Khichdi, fruits, and Kuttu.",
        "dress": "Elaborate, colorful traditional attire like Chaniya Choli, Kurta Pajamas, and Sarees.",
        "ritual": "Daily Aarti, fasting, and reading of the Durga Saptashati.",
        "hindi_why": "{state} भर में देवी दुर्गा के नौ रूपों को समर्पित नौ रातें।",
        "hindi_how": "सामुदायिक नृत्य (जैसे गरबा/डांडिया), उपवास, और विस्तृत पंडाल भ्रमण।",
        "hindi_food": "पूरी तरह से शाकाहारी, उपवास का भोजन (व्रत का खाना) जैसे साबूदाना खिचड़ी, फल और कुट्टू।",
        "hindi_dress": "विस्तृत, रंगीन पारंपरिक परिधान जैसे चनिया चोली, कुर्ता पजामा और साड़ियां।",
        "hindi_ritual": "दैनिक आरती, उपवास, और दुर्गा सप्तशती का पाठ।"
    },
    {
        "name_template": "Deepavali Mela {state}",
        "religion": "Hindu/Cultural",
        "month": "November",
        "startDate": "2026-11-01",
        "endDate": "2026-11-03",
        "why": "The festival of lights, representing the victory of light over darkness in {state}.",
        "how": "Illuminating homes with clay lamps (diyas), fireworks, and exchanging gifts.",
        "food": "An abundance of rich sweets like Kaju Katli, Laddoos, and savory snacks.",
        "dress": "New traditional clothes purchased specifically for the auspicious day.",
        "ritual": "Lakshmi Puja in the evening to welcome prosperity and wealth.",
        "hindi_why": "रोशनी का त्योहार, जो {state} में अंधकार पर प्रकाश की जीत का प्रतिनिधित्व करता है।",
        "hindi_how": "मिट्टी के दीयों (दीये) से घरों को रोशन करना, आतिशबाजी करना और उपहारों का आदान-प्रदान करना।",
        "hindi_food": "काजू कतली, लड्डू और स्वादिष्ट स्नैक्स जैसी समृद्ध मिठाइयों की बहुतायत।",
        "hindi_dress": "विशेष रूप से शुभ दिन के लिए खरीदे गए नए पारंपरिक कपड़े।",
        "hindi_ritual": "समृद्धि और धन के स्वागत के लिए शाम को लक्ष्मी पूजा।"
    },
    {
        "name_template": "Regional Food & Spice Festival {state}",
        "religion": "Cultural",
        "month": "February",
        "startDate": "2026-02-12",
        "endDate": "2026-02-16",
        "why": "Celebrating the unique culinary heritage and local spices of {state}.",
        "how": "Cooking competitions, food tasting stalls, and demonstrations by regional chefs.",
        "food": "Every regional specialty of {state} is available in one place.",
        "dress": "Casual wear suitable for walking and eating in large crowds.",
        "ritual": "Culinary workshops and sharing of generational family recipes.",
        "hindi_why": "{state} की अनूठी पाक विरासत और स्थानीय मसालों का जश्न।",
        "hindi_how": "खाना पकाने की प्रतियोगिताएं, खाद्य चखने के स्टॉल और क्षेत्रीय शेफ द्वारा प्रदर्शन।",
        "hindi_food": "{state} की हर क्षेत्रीय विशेषता एक ही स्थान पर उपलब्ध है।",
        "hindi_dress": "बड़ी भीड़ में चलने और खाने के लिए उपयुक्त आरामदायक परिधान।",
        "hindi_ritual": "पाक कार्यशालाएं और पीढ़ीगत पारिवारिक व्यंजनों को साझा करना।"
    },
    {
        "name_template": "Local Deity Rath Yatra {state}",
        "religion": "Hindu",
        "month": "June-July",
        "startDate": "2026-06-25",
        "endDate": "2026-06-25",
        "why": "Annual procession of the regional patron deity of {state}.",
        "how": "Pulling of massive wooden chariots by thousands of devotees accompanied by loud devotional music.",
        "food": "Temple prasadam (consecrated food) distributed freely among the massive crowds.",
        "dress": "Traditional devotional attire; men often bare-chested or in simple dhotis, women in simple sarees.",
        "ritual": "Chariot pulling, continuous chanting, and offering prayers to the deity as it tours the city.",
        "hindi_why": "{state} के क्षेत्रीय संरक्षक देवता का वार्षिक जुलूस।",
        "hindi_how": "जोरदार भक्ति संगीत के साथ हजारों भक्तों द्वारा विशाल लकड़ी के रथों को खींचना।",
        "hindi_food": "विशाल भीड़ के बीच स्वतंत्र रूप से वितरित मंदिर प्रसाद (पवित्र भोजन)।",
        "hindi_dress": "पारंपरिक भक्ति परिधान; पुरुष अक्सर नंगे बदन या साधारण धोती में, महिलाएं साधारण साड़ियों में।",
        "hindi_ritual": "रथ खींचना, निरंतर जप, और देवता की पूजा करना क्योंकि यह शहर का भ्रमण करता है।"
    }
]

new_festivals = []
# Ensure IDs don't collide
start_id = max([f['id'] for f in existing_data], default=0) + 1

for state, coords in states_data.items():
    for t in templates:
        # Add slight jitter to coordinates so they spread out over the state
        lat_jitter = random.uniform(-1.5, 1.5)
        lng_jitter = random.uniform(-1.5, 1.5)
        
        fest = {
            "id": start_id,
            "festivalName": t["name_template"].format(state=state),
            "religion": t["religion"],
            "month": t["month"],
            "state": state,
            "startDate": t["startDate"],
            "endDate": t["endDate"],
            "lat": coords["lat"] + lat_jitter,
            "lng": coords["lng"] + lng_jitter,
            "externalLink": "",
            "shortInfo": {
                "why": t["why"].format(state=state),
                "how": t["how"].format(state=state),
                "food": t["food"].format(state=state),
                "dress": t["dress"].format(state=state),
                "ritual": t["ritual"].format(state=state)
            },
            "hindiDescription": {
                "why": t["hindi_why"].format(state=state),
                "how": t["hindi_how"].format(state=state),
                "food": t["hindi_food"].format(state=state),
                "dress": t["hindi_dress"].format(state=state),
                "ritual": t["hindi_ritual"].format(state=state)
            }
        }
        new_festivals.append(fest)
        start_id += 1

existing_data.extend(new_festivals)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(existing_data, f, indent=2, ensure_ascii=False)

print(f"Successfully generated {len(new_festivals)} new festivals. Total is now {len(existing_data)}.")
