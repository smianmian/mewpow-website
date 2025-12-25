import json

# Translation Dictionaries
CATEGORIES = {
    "humidifier": {"zh": "加湿器", "en": "Humidifier", "ja": "加湿器", "ko": "가습기", "de": "Luftbefeuchter", "fr": "Humidificateur", "es": "Humidificador", "zh-TW": "加濕器"},
    "hairdryer": {"zh": "吹风机", "en": "Hair Dryer", "ja": "ヘアドライヤー", "ko": "헤어 드라이어", "de": "Haartrockner", "fr": "Sèche-Cheveux", "es": "Secador de Pelo", "zh-TW": "吹風機"},
    "heater": {"zh": "取暖器", "en": "Heater", "ja": "ヒーター", "ko": "히터", "de": "Heizgerät", "fr": "Chauffage", "es": "Calentador", "zh-TW": "取暖器"},
    "fan": {"zh": "风扇", "en": "Fan", "ja": "扇風機", "ko": "선풍기", "de": "Ventilator", "fr": "Ventilateur", "es": "Ventilador", "zh-TW": "風扇"},
    "purifier": {"zh": "空气净化器", "en": "Air Purifier", "ja": "空気清浄機", "ko": "공기 청정기", "de": "Luftreiniger", "fr": "Purificateur d'Air", "es": "Purificador de Aire", "zh-TW": "空氣淨化器"},
    "toothbrush": {"zh": "电动牙刷", "en": "Electric Toothbrush", "ja": "電動歯ブラシ", "ko": "전동 칫솔", "de": "Elektrische Zahnbürste", "fr": "Brosse à Dents Électrique", "es": "Cepillo Eléctrico", "zh-TW": "電動牙刷"},
    "shoedryer": {"zh": "烘鞋器", "en": "Shoe Dryer", "ja": "靴乾燥機", "ko": "신발 건조기", "de": "Schuhtrockner", "fr": "Sèche-Chaussures", "es": "Secador de Zapatos", "zh-TW": "烘鞋器"},
    "mosquito": {"zh": "灭蚊灯", "en": "Mosquito Lamp", "ja": "蚊取りランプ", "ko": "모기 램프", "de": "Mückenlampe", "fr": "Lampe Anti-Moustiques", "es": "Lámpara Antimosquitos", "zh-TW": "滅蚊燈"},
    "trimmer": {"zh": "毛球修剪器", "en": "Fabric Shaver", "ja": "毛玉取り器", "ko": "보풀 제거기", "de": "Fusselrasierer", "fr": "Anti-Bouloches", "es": "Quitapelusas", "zh-TW": "毛球修剪器"}
}

SPECS_DICT = {
    "Color": {"zh": "颜色", "en": "Color", "ja": "カラー", "ko": "색상", "de": "Farbe", "fr": "Couleur", "es": "Color", "zh-TW": "顏色"},
    "White": {"zh": "白色", "en": "White", "ja": "ホワイト", "ko": "화이트", "de": "Weiß", "fr": "Blanc", "es": "Blanco", "zh-TW": "白色"},
    "Pink": {"zh": "粉色", "en": "Pink", "ja": "ピンク", "ko": "핑크", "de": "Rosa", "fr": "Rose", "es": "Rosa", "zh-TW": "粉色"},
    "Blue": {"zh": "蓝色", "en": "Blue", "ja": "ブルー", "ko": "블루", "de": "Blau", "fr": "Bleu", "es": "Azul", "zh-TW": "藍色"},
    "Green": {"zh": "绿色", "en": "Green", "ja": "グリーン", "ko": "그린", "de": "Grün", "fr": "Vert", "es": "Verde", "zh-TW": "綠色"},
    "Black": {"zh": "黑色", "en": "Black", "ja": "ブラック", "ko": "블랙", "de": "Schwarz", "fr": "Noir", "es": "Negro", "zh-TW": "黑色"},
    "Battery": {"zh": "电池", "en": "Battery", "ja": "バッテリー", "ko": "배터리", "de": "Akku", "fr": "Batterie", "es": "Batería", "zh-TW": "電池"},
    "Material": {"zh": "材质", "en": "Material", "ja": "素材", "ko": "소재", "de": "Material", "fr": "Matériau", "es": "Material", "zh-TW": "材質"},
    "Power": {"zh": "功率", "en": "Power", "ja": "出力", "ko": "전력", "de": "Leistung", "fr": "Puissance", "es": "Potencia", "zh-TW": "功率"},
    "Voltage": {"zh": "电压", "en": "Voltage", "ja": "電圧", "ko": "전압", "de": "Spannung", "fr": "Tension", "es": "Voltaje", "zh-TW": "電壓"},
    "Capacity": {"zh": "容量", "en": "Capacity", "ja": "容量", "ko": "용량", "de": "Kapazität", "fr": "Capacité", "es": "Capacidad", "zh-TW": "容量"},
    "Rechargeable": {"zh": "充电款", "en": "Rechargeable", "ja": "充電式", "ko": "충전식", "de": "Aufladbar", "fr": "Rechargeable", "es": "Recargable", "zh-TW": "充電款"},
    "USB Powered": {"zh": "USB供电", "en": "USB Powered", "ja": "USB給電", "ko": "USB 전원", "de": "USB-Betrieb", "fr": "Alimenté par USB", "es": "Alimentado por USB", "zh-TW": "USB供電"},
    "Silent": {"zh": "静音", "en": "Silent", "ja": "静音", "ko": "저소음", "de": "Leise", "fr": "Silencieux", "es": "Silencioso", "zh-TW": "靜音"},
    "Portable": {"zh": "便携", "en": "Portable", "ja": "ポータブル", "ko": "휴대용", "de": "Tragbar", "fr": "Portable", "es": "Portátil", "zh-TW": "便攜"},
    "Smart": {"zh": "智能", "en": "Smart", "ja": "スマート", "ko": "스마트", "de": "Smart", "fr": "Intelligent", "es": "Inteligente", "zh-TW": "智能"},
    "Timer": {"zh": "定时", "en": "Timer", "ja": "タイマー", "ko": "타이머", "de": "Timer", "fr": "Minuteur", "es": "Temporizador", "zh-TW": "定時"},
    "Remote Control": {"zh": "遥控", "en": "Remote Control", "ja": "リモコン", "ko": "리모컨", "de": "Fernbedienung", "fr": "Télécommande", "es": "Control Remoto", "zh-TW": "遙控"},
    "PTC Ceramic": {"zh": "PTC陶瓷发热", "en": "PTC Ceramic", "ja": "PTCセラミック", "ko": "PTC 세라믹", "de": "PTC-Keramik", "fr": "Céramique PTC", "es": "Cerámica PTC", "zh-TW": "PTC陶瓷發熱"},
    "Overheat Protection": {"zh": "过热保护", "en": "Overheat Protection", "ja": "過熱保護", "ko": "과열 보호", "de": "Überhitzungsschutz", "fr": "Protection Surchauffe", "es": "Protección Sobrecalentamiento", "zh-TW": "過熱保護"},
    "Energy Efficient": {"zh": "节能", "en": "Energy Efficient", "ja": "省エネ", "ko": "에너지 효율", "de": "Energieeffizient", "fr": "Économe en Énergie", "es": "Eficiencia Energética", "zh-TW": "節能"},
    "UV Light": {"zh": "UV杀菌", "en": "UV Light", "ja": "UVライト", "ko": "UV 라이트", "de": "UV-Licht", "fr": "Lumière UV", "es": "Luz UV", "zh-TW": "UV殺菌"},
    "HEPA Filter": {"zh": "HEPA滤网", "en": "HEPA Filter", "ja": "HEPAフィルター", "ko": "HEPA 필터", "de": "HEPA-Filter", "fr": "Filtre HEPA", "es": "Filtro HEPA", "zh-TW": "HEPA濾網"},
    "Ionic Technology": {"zh": "负离子技术", "en": "Ionic Technology", "ja": "イオン技術", "ko": "이온 기술", "de": "Ionen-Technologie", "fr": "Technologie Ionique", "es": "Tecnología Iónica", "zh-TW": "負離子技術"},
    "Foldable": {"zh": "可折叠", "en": "Foldable", "ja": "折りたたみ式", "ko": "접이식", "de": "Faltbar", "fr": "Pliable", "es": "Plegable", "zh-TW": "可折疊"},
    "Lightweight": {"zh": "轻量化", "en": "Lightweight", "ja": "軽量", "ko": "경량", "de": "Leichtgewicht", "fr": "Léger", "es": "Ligero", "zh-TW": "輕量化"},
    "Dual Voltage": {"zh": "双电压", "en": "Dual Voltage", "ja": "デュアル電圧", "ko": "듀얼 전압", "de": "Doppelspannung", "fr": "Double Tension", "es": "Doble Voltaje", "zh-TW": "雙電壓"},
    "Compact Design": {"zh": "紧凑设计", "en": "Compact Design", "ja": "コンパクト設計", "ko": "컴팩트 디자인", "de": "Kompaktes Design", "fr": "Design Compact", "es": "Diseño Compacto", "zh-TW": "緊湊設計"},
    "Brushless Motor": {"zh": "无刷电机", "en": "Brushless Motor", "ja": "ブラシレスモーター", "ko": "브러시리스 모터", "de": "Bürstenloser Motor", "fr": "Moteur Sans Balais", "es": "Motor Sin Escobillas", "zh-TW": "無刷電機"},
    "Oscillating": {"zh": "摇头", "en": "Oscillating", "ja": "首振り", "ko": "회전", "de": "Oszillierend", "fr": "Oscillant", "es": "Oscilante", "zh-TW": "搖頭"},
    "Digital Display": {"zh": "数显", "en": "Digital Display", "ja": "デジタル表示", "ko": "디지털 디스플레이", "de": "Digitalanzeige", "fr": "Affichage Numérique", "es": "Pantalla Digital", "zh-TW": "數顯"},
    "DC Motor": {"zh": "直流电机", "en": "DC Motor", "ja": "DCモーター", "ko": "DC 모터", "de": "DC-Motor", "fr": "Moteur DC", "es": "Motor DC", "zh-TW": "直流電機"},
    "Sleep Mode": {"zh": "睡眠模式", "en": "Sleep Mode", "ja": "睡眠モード", "ko": "수면 모드", "de": "Schlafmodus", "fr": "Mode Veille", "es": "Modo Sueño", "zh-TW": "睡眠模式"},
    "360° Rotation": {"zh": "360°旋转", "en": "360° Rotation", "ja": "360°回転", "ko": "360° 회전", "de": "360° Rotation", "fr": "Rotation 360°", "es": "Rotación 360°", "zh-TW": "360°旋轉"},
    "Quiet Operation": {"zh": "静音运行", "en": "Quiet Operation", "ja": "静音運転", "ko": "조용한 작동", "de": "Leiser Betrieb", "fr": "Fonctionnement Silencieux", "es": "Funcionamiento Silencioso", "zh-TW": "靜音運行"},
    "Smart Sensor": {"zh": "智能传感器", "en": "Smart Sensor", "ja": "スマートセンサー", "ko": "스마트 센서", "de": "Intelligenter Sensor", "fr": "Capteur Intelligent", "es": "Sensor Inteligente", "zh-TW": "智能傳感器"},
    "App Control": {"zh": "APP控制", "en": "App Control", "ja": "アプリ制御", "ko": "앱 제어", "de": "App-Steuerung", "fr": "Contrôle par App", "es": "Control por App", "zh-TW": "APP控制"},
    "H13 HEPA": {"zh": "H13级HEPA", "en": "H13 HEPA", "ja": "H13 HEPA", "ko": "H13 HEPA", "de": "H13 HEPA", "fr": "H13 HEPA", "es": "H13 HEPA", "zh-TW": "H13級HEPA"},
    "UV-C Light": {"zh": "UV-C杀菌", "en": "UV-C Light", "ja": "UV-Cライト", "ko": "UV-C 라이트", "de": "UV-C Licht", "fr": "Lumière UV-C", "es": "Luz UV-C", "zh-TW": "UV-C殺菌"},
    "Air Quality Display": {"zh": "空气质量显示", "en": "Air Quality Display", "ja": "空気質表示", "ko": "공기질 표시", "de": "Luftqualitätsanzeige", "fr": "Affichage Qualité Air", "es": "Pantalla Calidad Aire", "zh-TW": "空氣質量顯示"},
    "IPX7 Waterproof": {"zh": "IPX7防水", "en": "IPX7 Waterproof", "ja": "IPX7防水", "ko": "IPX7 방수", "de": "IPX7 Wasserdicht", "fr": "Étanche IPX7", "es": "Impermeable IPX7", "zh-TW": "IPX7防水"},
    "30-Day Battery": {"zh": "30天续航", "en": "30-Day Battery", "ja": "30日間のバッテリー", "ko": "30일 배터리", "de": "30-Tage-Akku", "fr": "Batterie 30 Jours", "es": "Batería 30 Días", "zh-TW": "30天續航"},
    "5 Modes": {"zh": "5种模式", "en": "5 Modes", "ja": "5つのモード", "ko": "5가지 모드", "de": "5 Modi", "fr": "5 Modes", "es": "5 Modos", "zh-TW": "5種模式"},
    "USB Charging": {"zh": "USB充电", "en": "USB Charging", "ja": "USB充電", "ko": "USB 충전", "de": "USB-Laden", "fr": "Chargement USB", "es": "Carga USB", "zh-TW": "USB充電"},
    "PTC Heating": {"zh": "PTC发热", "en": "PTC Heating", "ja": "PTC加熱", "ko": "PTC 가열", "de": "PTC-Heizung", "fr": "Chauffage PTC", "es": "Calefacción PTC", "zh-TW": "PTC發熱"},
    "Timer Function": {"zh": "定时功能", "en": "Timer Function", "ja": "タイマー機能", "ko": "타이머 기능", "de": "Timer-Funktion", "fr": "Fonction Minuteur", "es": "Función Temporizador", "zh-TW": "定時功能"},
    "Sterilization": {"zh": "杀菌", "en": "Sterilization", "ja": "殺菌", "ko": "살균", "de": "Sterilisation", "fr": "Stérilisation", "es": "Esterilización", "zh-TW": "殺菌"},
    "Anti-slip Base": {"zh": "防滑底座", "en": "Anti-slip Base", "ja": "滑り止めベース", "ko": "미끄럼 방지 베이스", "de": "Rutschfeste Basis", "fr": "Base Antidérapante", "es": "Base Antideslizante", "zh-TW": "防滑底座"},
    "Silent Operation": {"zh": "静音运行", "en": "Silent Operation", "ja": "静音運転", "ko": "조용한 작동", "de": "Leiser Betrieb", "fr": "Fonctionnement Silencieux", "es": "Funcionamiento Silencioso", "zh-TW": "靜音運行"},
    "Reusable Trap": {"zh": "可重复使用", "en": "Reusable Trap", "ja": "再利用可能なトラップ", "ko": "재사용 가능한 트랩", "de": "Wiederverwendbare Falle", "fr": "Piège Réutilisable", "es": "Trampa Reutilizable", "zh-TW": "可重複使用"},
    "3-blade System": {"zh": "三叶刀头", "en": "3-blade System", "ja": "3枚刃システム", "ko": "3날 시스템", "de": "3-Klingen-System", "fr": "Système 3 Lames", "es": "Sistema de 3 Cuchillas", "zh-TW": "三葉刀頭"},
    "LED Display": {"zh": "LED显示", "en": "LED Display", "ja": "LED表示", "ko": "LED 디스플레이", "de": "LED-Anzeige", "fr": "Affichage LED", "es": "Pantalla LED", "zh-TW": "LED顯示"}
}

def translate_text(text, target_lang):
    # Try exact match in SPECS_DICT
    if text in SPECS_DICT and target_lang in SPECS_DICT[text]:
        return SPECS_DICT[text][target_lang]
    
    # Try partial match (e.g. "2000W Power" -> "2000W" + "Power")
    # This is a simple heuristic
    for key, translations in SPECS_DICT.items():
        if key in text and target_lang in translations:
            return text.replace(key, translations[target_lang])
            
    return text # Fallback to original

def process_products():
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            products = json.load(f)
    except FileNotFoundError:
        print("products.json not found")
        return

    updated_products = []
    
    for p in products:
        # Ensure 'names' object exists
        if 'names' not in p:
            p['names'] = {}
            
        # Ensure 'specs' object exists (convert from array if needed)
        if isinstance(p.get('specs'), list):
            original_specs = p['specs']
            p['specs'] = {}
            # Use original specs as English base if they look English, or Chinese if Chinese
            # Simple check: if any Chinese char, assume Chinese base
            is_chinese = any(u'\u4e00' <= c <= u'\u9fff' for c in str(original_specs))
            base_lang = 'zh' if is_chinese else 'en'
            p['specs'][base_lang] = original_specs
            
        # 1. Translate Name
        # Use category name as base if name is generic
        base_name = p.get('name', '') or p['names'].get('en', '') or p['names'].get('zh', '')
        
        for lang in ['en', 'zh', 'ja', 'ko', 'de', 'fr', 'es', 'zh-TW']:
            if lang not in p['names'] or not p['names'][lang]:
                # Try to generate a name
                # E.g. "Humidifier X1" -> "加湿器 X1"
                cat_key = p.get('category', '')
                if cat_key in CATEGORIES:
                    cat_name = CATEGORIES[cat_key][lang]
                    # If base name contains English category name, replace it
                    en_cat = CATEGORIES[cat_key]['en']
                    if en_cat in base_name:
                        p['names'][lang] = base_name.replace(en_cat, cat_name)
                    else:
                        # Just append model number to category name
                        model = p.get('model', '') or p.get('id', '').split('-')[-1].upper()
                        p['names'][lang] = f"{cat_name} {model}"
                else:
                    p['names'][lang] = base_name # Fallback

        # 2. Translate Specs
        # Get the base specs list (prefer English, then Chinese)
        base_specs = p['specs'].get('en') or p['specs'].get('zh') or []
        
        for lang in ['en', 'zh', 'ja', 'ko', 'de', 'fr', 'es', 'zh-TW']:
            if lang not in p['specs']:
                p['specs'][lang] = []
                for spec in base_specs:
                    p['specs'][lang].append(translate_text(spec, lang))
                    
        # Ensure certifications exist
        if 'certifications' not in p:
            p['certifications'] = {'ce': True, 'rohs': True, 'iso9001': True}
            
        updated_products.append(p)

    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(updated_products, f, indent=4, ensure_ascii=False)
    
    print(f"Processed {len(updated_products)} products.")

if __name__ == "__main__":
    process_products()
