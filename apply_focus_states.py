import json

festivals_data = [
    # --- BIHAR ---
    {
        "id": 1,
        "festivalName": "Chhath Puja",
        "religion": "Hindu",
        "month": "October-November",
        "state": "Bihar",
        "startDate": "2026-11-15",
        "endDate": "2026-11-18",
        "lat": 25.5941,
        "lng": 85.1376, # Patna
        "externalLink": "https://tourism.bihar.gov.in/en/destinations/patna/chhath-puja",
        "shortInfo": {
            "why": "Dedicated to the Sun God (Surya) and Chhathi Maiya for thanking them for sustaining life on earth.",
            "how": "Rigorous four-day fasting, holy bathing, and offering 'Arghya' to the setting and rising sun while standing in a water body.",
            "food": "Thekua, Khajuria, Kasar, and fruits offered as prasad.",
            "dress": "Traditional cotton or silk sarees (without stitched borders) for women, dhoti for men.",
            "ritual": "Vrittis (devotees) fast without water and observe strict purity. No idol worship."
        },
        "hindiDescription": {
            "why": "पृथ्वी पर जीवन को बनाए रखने के लिए सूर्य देव (सूर्य) और छठी मैया को समर्पित।",
            "how": "कठोर चार दिवसीय उपवास, पवित्र स्नान, और जलाशय में खड़े होकर डूबते और उगते सूर्य को 'अर्घ्य' देना।",
            "food": "ठेकुआ, खजूरिया, कसार और प्रसाद के रूप में चढ़ाए जाने वाले फल।",
            "dress": "महिलाओं के लिए पारंपरिक सूती या रेशमी साड़ियाँ, पुरुषों के लिए धोती।",
            "ritual": "भक्त बिना पानी के उपवास करते हैं और सख्त पवित्रता का पालन करते हैं। कोई मूर्ति पूजा नहीं।"
        }
    },
    {
        "id": 2,
        "festivalName": "Sonepur Cattle Fair",
        "religion": "Cultural/Hindu",
        "month": "November",
        "state": "Bihar",
        "startDate": "2026-11-20",
        "endDate": "2026-12-10",
        "lat": 25.6885,
        "lng": 85.1764, # Sonepur
        "externalLink": "https://tourism.bihar.gov.in/en/destinations/saran/sonepur-mela",
        "shortInfo": {
            "why": "Asia's largest cattle fair, beginning on Kartik Purnima.",
            "how": "Extensive animal trading, cultural performances, circus, and rural exhibitions.",
            "food": "Litti Chokha, Jalebis, and various sweetmeats prevalent in rural melas.",
            "dress": "Casual and traditional rural attire.",
            "ritual": "Taking a holy dip at the confluence of the Ganges and Gandak rivers and praying at Hariharnath temple."
        },
         "hindiDescription": {
            "why": "एशिया का सबसे बड़ा पशु मेला, कार्तिक पूर्णिमा से शुरू होता है।",
            "how": "व्यापक पशु व्यापार, सांस्कृतिक प्रदर्शन, सर्कस और ग्रामीण प्रदर्शनियां।",
            "food": "लिट्टी चोखा, जलेबी, और ग्रामीण मेलों में प्रचलित विभिन्न मिठाइयाँ।",
            "dress": "आरामदायक और पारंपरिक ग्रामीण पोशाक।",
            "ritual": "गंगा और गंडक नदियों के संगम पर पवित्र स्नान करना और हरिहरनाथ मंदिर में प्रार्थना करना।"
        }
    },
    {
        "id": 3,
        "festivalName": "Makar Sankranti (Khichdi Mela)",
        "religion": "Hindu",
        "month": "January",
        "state": "Bihar",
        "startDate": "2026-01-14",
        "endDate": "2026-01-15",
        "lat": 24.8143,
        "lng": 87.0392, # Mandar Hills / Banka
        "externalLink": "",
        "shortInfo": {
            "why": "Marks the end of winter and the transition of the sun into Capricorn.",
            "how": "Holy dips in rivers, kite flying, and large fairs like the one at Mandar Hills.",
            "food": "Dahi-Chura (curd and flattened rice), Khichdi, and Tilkut (sesame sweets).",
            "dress": "Traditional warm winter clothing.",
            "ritual": "Bathing in hot springs or holy water, offering prayers and flowers."
        },
         "hindiDescription": {
            "why": "सर्दियों के अंत और मकर राशि में सूर्य के प्रवेश का प्रतीक है।",
            "how": "नदियों में पवित्र डुबकी, पतंगबाजी, और मंदार हिल्स जैसे बड़े मेले।",
            "food": "दही-चूड़ा, खिचड़ी, और तिलकुट (तिल की मिठाई)।",
            "dress": "पारंपरिक गर्म सर्दियों के कपड़े।",
            "ritual": "गर्म झरनों या पवित्र जल में स्नान करना, प्रार्थना और फूल चढ़ाना।"
        }
    },
    {
        "id": 4,
        "festivalName": "Pitrapaksha Mela",
        "religion": "Hindu",
        "month": "September",
        "state": "Bihar",
        "startDate": "2026-09-06",
        "endDate": "2026-09-21",
        "lat": 24.7914,
        "lng": 85.0002, # Gaya
        "externalLink": "https://tourism.bihar.gov.in/en/destinations/gaya",
        "shortInfo": {
            "why": "A fortnight dedicated to honoring ancestors and departed souls.",
            "how": "Thousands converge in Gaya to perform 'Pind Daan' along the banks of the Falgu River.",
            "food": "Satvik food; fasting is common during the specific ritual days.",
            "dress": "Simple, traditional attire, usually white or dull colors during rituals.",
            "ritual": "Offering 'Pind' (rice balls) and performing Shraddha ceremonies for the peace of ancestors."
        },
        "hindiDescription": {
             "why": "पूर्वजों और दिवंगत आत्माओं का सम्मान करने के लिए समर्पित एक पखवाड़ा।",
            "how": "हजारों लोग फल्गु नदी के तट पर 'पिंड दान' करने के लिए गया में इकट्ठा होते हैं।",
            "food": "सात्विक भोजन; विशिष्ट अनुष्ठान के दिनों में उपवास आम है।",
            "dress": "सरल, पारंपरिक पोशाक, आमतौर पर अनुष्ठानों के दौरान सफेद।",
            "ritual": "पित्रों की शांति के लिए 'पिंड' (चावल के गोले) चढ़ाना और श्राद्ध समारोह करना।"
        }
    },
    {
        "id": 5,
        "festivalName": "Rajgir Mahotsav",
        "religion": "Cultural",
        "month": "October-November",
        "state": "Bihar",
        "startDate": "2026-11-25",
        "endDate": "2026-11-27",
        "lat": 25.0294,
        "lng": 85.4190, # Rajgir
        "externalLink": "https://tourism.bihar.gov.in/en/destinations/nalanda/rajgir",
        "shortInfo": {
            "why": "Celebrates the rich cultural, historical, and religious heritage of Rajgir.",
            "how": "Three-day festival featuring classical music, folk dances, and cultural stalls.",
            "food": "Local Bihari cuisine featured in various food stalls.",
            "dress": "Festive and casual wear.",
            "ritual": "A cultural celebration drawing both Jain and Buddhist communities, promoting peace and heritage."
        },
         "hindiDescription": {
             "why": "राजगीर की समृद्ध सांस्कृतिक, ऐतिहासिक और धार्मिक विरासत का जश्न मनाता है।",
            "how": "तीन दिवसीय उत्सव जिसमें शास्त्रीय संगीत, लोक नृत्य और सांस्कृतिक स्टॉल शामिल हैं।",
            "food": "विभिन्न फूड स्टालों में स्थानीय बिहारी व्यंजन।",
            "dress": "उत्सव और आकस्मिक परिधान।",
            "ritual": "एक सांस्कृतिक उत्सव जो जैन और बौद्ध दोनों समुदायों को आकर्षित करता है, शांति और विरासत को बढ़ावा देता है।"
        }
    },
    {
        "id": 6,
        "festivalName": "Buddha Jayanti",
        "religion": "Buddhist",
        "month": "May",
        "state": "Bihar",
        "startDate": "2026-05-01",
        "endDate": "2026-05-01",
        "lat": 24.6961,
        "lng": 84.9869, # Bodh Gaya
        "externalLink": "https://tourism.bihar.gov.in/en/destinations/gaya/mahabodhi-temple",
        "shortInfo": {
            "why": "Commemorates the birth, enlightenment, and passing away of Gautama Buddha.",
            "how": "Massive gatherings at the Mahabodhi Temple, reading of scriptures, and peaceful processions.",
            "food": "Kheer (sweet rice porridge) is traditionally served.",
            "dress": "Simple white or light-colored clothing.",
            "ritual": "Bathing the Buddha idol, offering flowers and candles, and observing precepts."
        },
        "hindiDescription": {
            "why": "गौतम बुद्ध के जन्म, ज्ञान प्राप्ति और महापरिनिर्वाण का स्मरण करता है।",
            "how": "महाबोधि मंदिर में भारी भीड़, शास्त्रों का पाठ और शांतिपूर्ण जुलूस।",
            "food": "पारंपरिक रूप से खीर (मीठे चावल का दलिया) परोसी जाती है।",
            "dress": "साधारण सफेद या हल्के रंग के कपड़े।",
            "ritual": "बुद्ध की मूर्ति को स्नान कराना, फूल और मोमबत्तियां चढ़ाना, और उपदेशों का पालन करना।"
        }
    },
    {
        "id": 7,
        "festivalName": "Bihula (Bishari Puja)",
        "religion": "Hindu/Folk",
        "month": "August",
        "state": "Bihar",
        "startDate": "2026-08-18",
        "endDate": "2026-08-18",
        "lat": 25.2425,
        "lng": 86.9842, # Bhagalpur
        "externalLink": "",
        "shortInfo": {
            "why": "Dedicated to Goddess Mansa, the snake goddess, for the protection of families.",
            "how": "Showcases the famous Manjusha art form, with elaborate storytelling of the Bihula folktale.",
            "food": "Traditional local sweets and offerings.",
            "dress": "Traditional Bihari saris and dhotis.",
            "ritual": "Worshipping the snake goddess and creating Manjusha art depictions of the lore."
        },
        "hindiDescription": {
             "why": "परिवारों की सुरक्षा के लिए नाग देवी, देवी मनसा को समर्पित।",
            "how": "बिहुला लोककथा के विस्तृत कहानी कहने के साथ प्रसिद्ध मंजूषा कला रूप को प्रदर्शित करता है।",
            "food": "पारंपरिक स्थानीय मिठाइयाँ और प्रसाद।",
            "dress": "पारंपरिक बिहारी साड़ी और धोती।",
            "ritual": "नाग देवी की पूजा करना और विद्या के मंजूषा कला चित्रण बनाना।"
        }
    },

    # --- JAMMU & KASHMIR ---
    {
        "id": 8,
        "festivalName": "Tulip Festival",
        "religion": "Cultural/Seasonal",
        "month": "April",
        "state": "Jammu & Kashmir",
        "startDate": "2026-04-05", # Varies slightly by bloom
        "endDate": "2026-04-25",
        "lat": 34.0869,
        "lng": 74.8778, # Srinagar Tulip Garden
        "externalLink": "https://www.jktourism.jk.gov.in/tulip.html",
        "shortInfo": {
            "why": "Celebrates the blooming of millions of tulips at Asia's largest tulip garden, signaling spring.",
            "how": "Visitors stroll through the Indira Gandhi Memorial Tulip Garden, enjoying cultural programs.",
            "food": "Kashmiri street food like Kahwa (saffron tea) and local breads.",
            "dress": "Comfortable spring attire; many rent traditional Kashmiri Pherans for photos.",
            "ritual": "A celebration of nature's beauty and the tourism revival in the Kashmir Valley."
        },
        "hindiDescription": {
            "why": "एशिया के सबसे बड़े ट्यूलिप गार्डन में लाखों ट्यूलिप के खिलने का जश्न मनाता है, जो वसंत का संकेत है।",
            "how": "आगंतुक सांस्कृतिक कार्यक्रमों का आनंद लेते हुए इंदिरा गांधी मेमोरियल ट्यूलिप गार्डन में टहलते हैं।",
            "food": "कश्मीरी स्ट्रीट फूड जैसे कहवा (केसर की चाय) और स्थानीय रोटियां।",
            "dress": "आरामदायक वसंत पोशाक; कई लोग तस्वीरों के लिए पारंपरिक कश्मीरी फेरन किराए पर लेते हैं।",
            "ritual": "प्रकृति की सुंदरता और कश्मीर घाटी में पर्यटन पुनरुद्धार का उत्सव।"
        }
    },
    {
        "id": 9,
        "festivalName": "Shikara Festival",
        "religion": "Cultural",
        "month": "July-August",
        "state": "Jammu & Kashmir",
        "startDate": "2026-07-20",
        "endDate": "2026-07-25",
        "lat": 34.1039,
        "lng": 74.8724, # Dal Lake
        "externalLink": "https://www.jktourism.jk.gov.in/shikara.html",
        "shortInfo": {
            "why": "Promotes tourism and celebrates the iconic Shikaras (traditional wooden boats) of Dal Lake.",
            "how": "Features Shikara races, decorated boat parades, and cultural music on floating stages.",
            "food": "Floating markets offer nadru (lotus stem) fries, kebabs, and tea.",
            "dress": "Casual boating attire; boatmen wear traditional Kashmiri garb.",
            "ritual": "A modern cultural festival preserving the unique water-based lifestyle of Srinagar."
        },
         "hindiDescription": {
            "why": "पर्यटन को बढ़ावा देता है और डल झील के प्रतिष्ठित शिकारों (पारंपरिक लकड़ी की नावों) का जश्न मनाता है।",
            "how": "तैरते हुए मंचों पर शिकारा दौड़, सजी हुई नाव परेड और सांस्कृतिक संगीत।",
            "food": "तैरते बाजार नदरू (कमल के तने) के फ्राई, कबाब और चाय पेश करते हैं।",
            "dress": "नौका विहार पोशाक; नाविक पारंपरिक कश्मीरी पोशाक पहनते हैं।",
            "ritual": "श्रीनगर की अनूठी जल-आधारित जीवन शैली को संरक्षित करने वाला एक आधुनिक सांस्कृतिक उत्सव।"
        }
    },
    {
        "id": 10,
        "festivalName": "Lohri",
        "religion": "Hindu/Sikh",
        "month": "January",
        "state": "Jammu & Kashmir",
        "startDate": "2026-01-13",
        "endDate": "2026-01-13",
        "lat": 32.7266,
        "lng": 74.8570, # Jammu
        "externalLink": "",
        "shortInfo": {
            "why": "Marks the end of peak winter and the harvest of Rabi crops, welcoming spring.",
            "how": "Lighting massive bonfires, singing traditional folk songs, and the 'Chajja' dance by boys.",
            "food": "Til (sesame), peanuts, jaggery, and corn.",
            "dress": "Bright, festive, warm traditional clothing.",
            "ritual": "Circumambulating the bonfire and offering winter crops to the fire deity."
        },
        "hindiDescription": {
            "why": "चरम सर्दियों के अंत और रबी फसलों की कटाई, वसंत का स्वागत करने का प्रतीक है।",
            "how": "विशाल अलाव जलाना, पारंपरिक लोक गीत गाना, और लड़कों द्वारा 'छज्जा' नृत्य।",
            "food": "तिल, मूंगफली, गुड़ और मक्का।",
            "dress": "उज्ज्वल, उत्सव, गर्म पारंपरिक कपड़े।",
            "ritual": "अलाव की परिक्रमा करना और अग्नि देवता को शीतकालीन फसलें चढ़ाना।"
        }
    },
    {
        "id": 11,
        "festivalName": "Shivratri (Herath)",
        "religion": "Hindu",
        "month": "February-March",
        "state": "Jammu & Kashmir",
        "startDate": "2026-02-15",
        "endDate": "2026-02-16",
        "lat": 32.7300,
        "lng": 74.8700, # Jammu temples (Peer Khoh etc)
        "externalLink": "",
        "shortInfo": {
            "why": "Dedicated to Lord Shiva, marking the convergence of Shiva and Shakti.",
            "how": "Night-long vigils, prayers, and colorful celebrations at temples like Peer Khoh in Jammu.",
            "food": "Walnuts are a significant part of the offerings; fasting is common.",
            "dress": "Traditional prayer attire.",
            "ritual": "Intricate poojas performed by Kashmiri Pandits involving soaked walnuts."
        },
        "hindiDescription": {
            "why": "भगवान शिव को समर्पित, शिव और शक्ति के अभिसरण को चिह्नित करता है।",
            "how": "रात भर जागरण, प्रार्थना, और जम्मू में पीर खोह जैसे मंदिरों में रंगीन उत्सव।",
            "food": "अखरोट प्रसाद का एक महत्वपूर्ण हिस्सा हैं; उपवास आम है।",
            "dress": "पारंपरिक प्रार्थना पोशाक।",
            "ritual": "कश्मीरी पंडितों द्वारा की जाने वाली जटिल पूजा जिसमें भीगे हुए अखरोट शामिल होते हैं।"
        }
    },
    {
        "id": 12,
        "festivalName": "Kheer Bhawani Festival",
        "religion": "Hindu",
        "month": "May-June",
        "state": "Jammu & Kashmir",
        "startDate": "2026-05-24",
        "endDate": "2026-05-24",
        "lat": 34.2257,
        "lng": 74.7578, # Ganderbal
        "externalLink": "",
        "shortInfo": {
            "why": "Celebrates the Goddess Ragnya Devi.",
            "how": "Massive gathering of Kashmiri Pandits at the Kheer Bhawani Temple in Tulmulla.",
            "food": "Milk and Kheer (rice pudding) are offered exclusively.",
            "dress": "Traditional attire.",
            "ritual": "Offering Kheer to the sacred spring, whose changing colors are believed to predict the region's future."
        },
        "hindiDescription": {
             "why": "देवी रागण्य देवी का उत्सव मनाता है।",
            "how": "तुलमुला में खीर भवानी मंदिर में कश्मीरी पंडितों का विशाल जमावड़ा।",
            "food": "प्रसाद के रूप में केवल दूध और खीर (चावल की खीर) चढ़ाई जाती है।",
            "dress": "पारंपरिक वेशभूषा।",
            "ritual": "पवित्र झरने में खीर चढ़ाना, जिसके बदलते रंगों को क्षेत्र के भविष्य की भविष्यवाणी माना जाता है।"
        }
    },
    {
        "id": 13,
        "festivalName": "Saffron Festival",
        "religion": "Cultural/Agricultural",
        "month": "November",
        "state": "Jammu & Kashmir",
        "startDate": "2026-11-05",
        "endDate": "2026-11-07",
        "lat": 34.0151,
        "lng": 74.9333, # Pampore
        "externalLink": "",
        "shortInfo": {
            "why": "Commemorates the harvesting season of Kashmir's world-famous saffron.",
            "how": "Cultural events, folk dances, and visits to the purple blooming saffron fields in Pampore.",
            "food": "Lots of Kahwa (saffron tea) and saffron-infused sweets.",
            "dress": "Casual outdoor wear.",
            "ritual": "Agricultural celebration highlighting the region's high-quality saffron production."
        },
        "hindiDescription": {
            "why": "कश्मीर के विश्व प्रसिद्ध केसर के कटाई के मौसम की याद दिलाता है।",
            "how": "सांस्कृतिक कार्यक्रम, लोक नृत्य, और पंपोर में बैंगनी खिलने वाले केसर के खेतों का दौरा।",
            "food": "बहुत सारी कहवा (केसर की चाय) और केसर युक्त मिठाइयाँ।",
            "dress": "आकस्मिक बाहरी पोशाक।",
            "ritual": "क्षेत्र के उच्च गुणवत्ता वाले केसर उत्पादन को उजागर करने वाला कृषि उत्सव।"
        }
    },
    {
        "id": 14,
        "festivalName": "Jhiri Fair",
        "religion": "Folk/Hindu",
        "month": "October-November",
        "state": "Jammu & Kashmir",
        "startDate": "2026-11-10",
        "endDate": "2026-11-18",
        "lat": 32.8468,
        "lng": 74.7431, # Jhiri Village
        "externalLink": "",
        "shortInfo": {
            "why": "Dedicated to Baba Jitu, a farmer who sacrificed his life fighting oppressive landlords.",
            "how": "Followers congregate from across North India in Jhiri village.",
            "food": "Locally grown produce and traditional Mela snacks.",
            "dress": "Rural agricultural and traditional wear.",
            "ritual": "Taking a dip in the Baba da Talab (pond) and honoring honesty and compassion."
        },
        "hindiDescription": {
            "why": "बाबा जित्तू को समर्पित, एक किसान जिसने दमनकारी जमींदारों से लड़ते हुए अपना जीवन बलिदान कर दिया।",
            "how": "अनुयायी पूरे उत्तर भारत से झिरी गांव में इकट्ठा होते हैं।",
            "food": "स्थानीय रूप से उगाई जाने वाली कृषि उपज और पारंपरिक मेले के स्नैक्स।",
            "dress": "ग्रामीण कृषि और पारंपरिक पोशाक।",
            "ritual": "बाबा दा तालाब (तालाब) में डुबकी लगाना और ईमानदारी और करुणा का सम्मान करना।"
        }
    },


    # --- RAJASTHAN ---
    {
        "id": 15,
        "festivalName": "Pushkar Camel Fair",
        "religion": "Cultural/Hindu",
        "month": "October-November",
        "state": "Rajasthan",
        "startDate": "2026-11-15",
        "endDate": "2026-11-23",
        "lat": 26.4883,
        "lng": 74.5509, # Pushkar
        "externalLink": "https://www.tourism.rajasthan.gov.in/pushkar-fair.html",
        "shortInfo": {
            "why": "A massive livestock trading fair aligning with the holy Kartik Purnima.",
            "how": "Trading of thousands of camels and horses, along with cultural performances, mustache competitions, and camel races.",
            "food": "Malpua, Kachori, and authentic Rajasthani thalis available across the fairgrounds.",
            "dress": "Extremely vibrant traditional Rajasthani attire; turbans (Safas) and Ghagra Cholis.",
            "ritual": "Pilgrims take a holy dip in Pushkar Lake, believed to cleanse sins."
        },
        "hindiDescription": {
             "why": "पवित्र कार्तिक पूर्णिमा के साथ संरेखित एक विशाल पशुधन व्यापार मेला।",
            "how": "हजारों ऊंटों और घोड़ों का व्यापार, साथ ही सांस्कृतिक प्रदर्शन, मूंछ प्रतियोगिताएं और ऊंट दौड़।",
            "food": "मालपुआ, कचौरी, और पूरे मेला मैदान में उपलब्ध प्रामाणिक राजस्थानी थाली।",
            "dress": "अत्यंत जीवंत पारंपरिक राजस्थानी पोशाक; पगड़ी (साफा) और घाघरा चोली।",
            "ritual": "तीर्थयात्री पुष्कर झील में पवित्र स्नान करते हैं, माना जाता है कि इससे पाप धुल जाते हैं।"
        }
    },
    {
        "id": 16,
        "festivalName": "Gangaur Festival",
        "religion": "Hindu",
        "month": "March-April",
        "state": "Rajasthan",
        "startDate": "2026-03-24",
        "endDate": "2026-04-10",
        "lat": 26.9124,
        "lng": 75.7873, # Jaipur
        "externalLink": "https://www.tourism.rajasthan.gov.in/gangaur-festival.html",
        "shortInfo": {
            "why": "Celebrated by women worshipping Goddess Parvati (Gauri) for marital bliss and well-being of husbands.",
            "how": "Women make clay idols of Gauri, dress up in fine clothes, and participate in grand processions.",
            "food": "Ghevar, a circular sweet disc made of flour and soaked in sugar syrup.",
            "dress": "Women wear bright, traditional Rajasthani outfits adorned with intricate jewelry.",
            "ritual": "Carrying images of Goddess Gauri on their heads through the streets."
        },
        "hindiDescription": {
            "why": "वैवाहिक आनंद और पति की भलाई के लिए देवी पार्वती (गौरी) की पूजा करने वाली महिलाओं द्वारा मनाया जाता है।",
            "how": "महिलाएं गौरी की मिट्टी की मूर्तियां बनाती हैं, सुंदर कपड़े पहनती हैं, और भव्य जुलूसों में भाग लेती हैं।",
            "food": "घेवर, आटे से बनी और चीनी की चाशनी में भिगोई हुई एक गोल मिठाई।",
            "dress": "महिलाएं जटिल गहनों से सजे उज्ज्वल, पारंपरिक राजस्थानी परिधान पहनती हैं।",
            "ritual": "सड़कों से होते हुए सिर पर देवी गौरी की मूर्तियाँ ले जाना।"
        }
    },
    {
        "id": 17,
        "festivalName": "International Kite Festival",
        "religion": "Cultural",
        "month": "January",
        "state": "Rajasthan",
        "startDate": "2026-01-14",
        "endDate": "2026-01-16",
        "lat": 26.9124,
        "lng": 75.7873, # Jaipur
        "externalLink": "https://www.tourism.rajasthan.gov.in/kite-festival.html",
        "shortInfo": {
            "why": "Coincides with Makar Sankranti, celebrating the sun's transition into the northern hemisphere.",
            "how": "The sky over Jaipur and Jodhpur is filled with thousands of kites. Competitions and illuminated night kite flying.",
            "food": "Til-laddoos (sesame seed sweets) and Gajak.",
            "dress": "Casual outdoor wear suitable for rooftops.",
            "ritual": "A day spent entirely on rooftops flying kites, shouting 'Woh Kaata' when cutting an opponent's string."
        },
        "hindiDescription": {
            "why": "मकर संक्रांति के साथ मेल खाता है, सूर्य के उत्तरी गोलार्ध में संक्रमण का जश्न मनाता है।",
            "how": "जयपुर और जोधपुर के ऊपर आसमान हजारों पतंगों से भर जाता है। प्रतियोगिताएं और रात में प्रबुद्ध पतंगबाजी।",
            "food": "तिल के लड्डू और गजक।",
            "dress": "छतों के लिए उपयुक्त आकस्मिक बाहरी पोशाक।",
            "ritual": "पूरा दिन छतों पर पतंग उड़ाने में बिताया, प्रतिद्वंद्वी की डोर काटने पर 'वो काटा' चिल्लाते हुए।"
        }
    },
    {
        "id": 18,
        "festivalName": "Teej Festival",
        "religion": "Hindu/Monsoon",
        "month": "July-August",
        "state": "Rajasthan",
        "startDate": "2026-08-15",
        "endDate": "2026-08-16",
        "lat": 26.9124,
        "lng": 75.7873, # Jaipur
        "externalLink": "https://www.tourism.rajasthan.gov.in/teej-festival.html",
        "shortInfo": {
            "why": "A monsoon festival dedicated to Goddess Parvati's reunion with Lord Shiva.",
            "how": "Grand 'Shahi Sawari' processions with decorated elephants, swinging on decorated swings, and singing traditional songs.",
            "food": "Ghevar and Malpua are essential Teej delicacies.",
            "dress": "Women predominantly wear green attire and apply Mehendi (henna).",
            "ritual": "Fasting and participating in the Goddess Parvati procession."
        },
         "hindiDescription": {
            "why": "देवी पार्वती के भगवान शिव के साथ पुनर्मिलन को समर्पित एक मानसून त्योहार।",
            "how": "सजे हुए हाथियों के साथ भव्य 'शाही सवारी' जुलूस, सजे हुए झूलों पर झूलना और पारंपरिक गीत गाना।",
            "food": "घेवर और मालपुआ आवश्यक तीज के व्यंजन हैं।",
            "dress": "महिलाएं मुख्य रूप से हरे रंग के कपड़े पहनती हैं और मेहंदी लगाती हैं।",
            "ritual": "उपवास और देवी पार्वती जुलूस में भाग लेना।"
        }
    },
    {
        "id": 19,
        "festivalName": "Bikaner Camel Festival",
        "religion": "Cultural",
        "month": "January",
        "state": "Rajasthan",
        "startDate": "2026-01-11",
        "endDate": "2026-01-12",
        "lat": 28.0229,
        "lng": 73.3119, # Bikaner
        "externalLink": "https://www.tourism.rajasthan.gov.in/bikaner-camel-festival.html",
        "shortInfo": {
            "why": "Celebrates the indispensable 'ship of the desert'.",
            "how": "Parade of beautifully decorated camels, camel milking, fur shearing competitions, and camel dances.",
            "food": "Unique food items made from camel milk, alongside traditional snacks.",
            "dress": "Traditional warm winter clothing for spectators.",
            "ritual": "Highlighting the grace and utility of camels in the harsh desert environment."
        },
        "hindiDescription": {
            "why": "अपरिहार्य 'रेगिस्तान के जहाज' का जश्न मनाता है।",
            "how": "खूबसूरती से सजाए गए ऊंटों की परेड, ऊंट का दूध निकालना, फर काटने की प्रतियोगिताएं और ऊंट नृत्य।",
            "food": "ऊंट के दूध से बने अनोखे खाद्य पदार्थ, पारंपरिक स्नैक्स के साथ।",
            "dress": "दर्शकों के लिए पारंपरिक गर्म सर्दियों के कपड़े।",
            "ritual": "कठोर रेगिस्तानी वातावरण में ऊंटों की कृपा और उपयोगिता को उजागर करना।"
        }
    },
    {
        "id": 20,
        "festivalName": "Mewar Festival",
        "religion": "Cultural",
        "month": "March-April",
        "state": "Rajasthan",
        "startDate": "2026-03-24",
        "endDate": "2026-03-26",
        "lat": 24.5854,
        "lng": 73.7125, # Udaipur
        "externalLink": "https://www.tourism.rajasthan.gov.in/mewar-festival.html",
        "shortInfo": {
            "why": "Welcomes the arrival of spring in the historic city of Udaipur, coinciding with Gangaur.",
            "how": "Women dress the images of Isar (Shiva) and Gangaur (Parvati) and carry them in a traditional procession through the city to Lake Pichola.",
            "food": "Traditional Mewari sweets and thalis.",
            "dress": "Colorful traditional attires, specifically bright turbans and ghagras.",
            "ritual": "Immersing the idols in Lake Pichola, followed by folk singing and a fireworks display."
        },
        "hindiDescription": {
             "why": "उदयपुर के ऐतिहासिक शहर में वसंत के आगमन का स्वागत करता है, जो गणगौर के साथ मेल खाता है।",
            "how": "महिलाएं ईसर (शिव) और गणगौर (पार्वती) की मूर्तियों को सजाती हैं और उन्हें शहर के माध्यम से पिछोला झील तक एक पारंपरिक जुलूस में ले जाती हैं।",
            "food": "पारंपरिक मेवाड़ी मिठाइयाँ और थालियाँ।",
            "dress": "रंगीन पारंपरिक परिधान, विशेष रूप से उज्ज्वल पगड़ी और घाघरा।",
            "ritual": "पिछोला झील में मूर्तियों का विसर्जन, उसके बाद लोक गायन और आतिशबाजी का प्रदर्शन।"
        }
    }
]

file_path = 'src/data/festivals.json'
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(festivals_data, f, indent=2, ensure_ascii=False)

print(f"Successfully wrote {len(festivals_data)} detailed festivals for Bihar, J&K, and Rajasthan.")
