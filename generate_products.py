#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
产品数据生成器
从产品信息.md生成完整的多语言产品JSON数据
"""

import json
import re

# 产品类别映射
CATEGORY_MAP = {
    "吹风机": "hairdryer",
    "取暖器": "heater", 
    "烘干器": "shoedryer",
    "毛球修剪器": "trimmer",
    "加湿器": "humidifier",
    "生活电器": "household",
    "电动牙具": "toothbrush",
    "空气净化器": "purifier",
    "风扇专场": "fan",
    "灭蚊灯拍": "mosquito"
}

# 多语言产品名称模板
def translate_product_name(zh_name, model, category):
    """生成多语言产品名称"""
    
    category_names = {
        "hairdryer": {
            "en": "Hair Dryer",
            "ja": "ヘアドライヤー",
            "de": "Haartrockner",
            "fr": "Sèche-Cheveux",
            "es": "Secador de Pelo"
        },
        "heater": {
            "en": "Heater",
            "ja": "ヒーター",
            "de": "Heizgerät",
            "fr": "Chauffage",
            "es": "Calentador"
        },
        "fan": {
            "en": "Fan",
            "ja": "扇風機",
            "de": "Ventilator",
            "fr": "Ventilateur",
            "es": "Ventilador"
        },
        "humidifier": {
            "en": "Humidifier",
            "ja": "加湿器",
            "de": "Luftbefeuchter",
            "fr": "Humidificateur",
            "es": "Humidificador"
        },
        "trimmer": {
            "en": "Fabric Shaver",
            "ja": "毛玉取り器",
            "de": "Fusselrasierer",
            "fr": "Anti-Bouloches",
            "es": "Quitapelusas"
        },
        "mosquito": {
            "en": "Mosquito Lamp",
            "ja": "蚊取りランプ",
            "de": "Mückenlampe",
            "fr": "Lampe Anti-Moustiques",
            "es": "Lámpara Antimosquitos"
        },
        "shoedryer": {
            "en": "Shoe Dryer",
            "ja": "靴乾燥機",
            "de": "Schuhtrockner",
            "fr": "Sèche-Chaussures",
            "es": "Secador de Zapatos"
        },
        "toothbrush": {
            "en": "Electric Toothbrush",
            "ja": "電動歯ブラシ",
            "de": "Elektrische Zahnbürste",
            "fr": "Brosse à Dents Électrique",
            "es": "Cepillo Eléctrico"
        },
        "purifier": {
            "en": "Air Purifier",
            "ja": "空気清浄機",
            "de": "Luftreiniger",
            "fr": "Purificateur d'Air",
            "es": "Purificador de Aire"
        },
        "household": {
            "en": "Household Appliance",
            "ja": "家電製品",
            "de": "Haushaltsgerät",
            "fr": "Appareil Électroménager",
            "es": "Electrodoméstico"
        }
    }
    
    names = {
        "zh": zh_name,
        "en": f"{category_names.get(category, {}).get('en', 'Product')} {model}",
        "ja": f"{category_names.get(category, {}).get('ja', '製品')} {model}",
        "de": f"{category_names.get(category, {}).get('de', 'Produkt')} {model}",
        "fr": f"{category_names.get(category, {}).get('fr', 'Produit')} {model}",
        "es": f"{category_names.get(category, {}).get('es', 'Producto')} {model}"
    }
    
    return names

# 生成产品规格的多语言版本
def translate_specs(specs_zh):
    """将中文规格翻译为多语言"""
    specs_multi = {
        "zh": specs_zh,
        "en": [],
        "ja": [],
        "de": [],
        "fr": [],
        "es": []
    }
    
    for spec in specs_zh:
        # 简单的关键词映射翻译
        if "无刷电机" in spec:
            specs_multi["en"].append(spec.replace("无刷电机", "Brushless Motor"))
            specs_multi["ja"].append(spec.replace("无刷电机", "ブラシレスモーター"))
            specs_multi["de"].append(spec.replace("无刷电机", "Bürstenloser Motor"))
            specs_multi["fr"].append(spec.replace("无刷电机", "Moteur Sans Balais"))
            specs_multi["es"].append(spec.replace("无刷电机", "Motor Sin Escobillas"))
        elif "有刷电机" in spec:
            specs_multi["en"].append(spec.replace("有刷电机", "Brushed Motor"))
            specs_multi["ja"].append(spec.replace("有刷电机", "ブラシモーター"))
            specs_multi["de"].append(spec.replace("有刷电机", "Bürstenmotor"))
            specs_multi["fr"].append(spec.replace("有刷电机", "Moteur à Balais"))
            specs_multi["es"].append(spec.replace("有刷电机", "Motor Con Escobillas"))
        else:
            # 保持原样或做简单处理
            specs_multi["en"].append(spec)
            specs_multi["ja"].append(spec)
            specs_multi["de"].append(spec)
            specs_multi["fr"].append(spec)
            specs_multi["es"].append(spec)
    
    return specs_multi

# 添加认证信息
def add_certifications(product):
    """为产品添加认证信息"""
    product["certifications"] = {
        "ce": True,
        "fcc": True,
        "rohs": True,
        "iso9001": True
    }
    product["features"] = {
        "eco_friendly": True,
        "innovative_rd": True,
        "quality_control": True
    }
    return product

print("产品数据生成器已准备就绪")
print("请手动运行此脚本以生成完整的产品数据")
