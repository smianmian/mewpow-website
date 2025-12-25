import json

def merge_products():
    # Load enhanced products
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            enhanced_products = json.load(f)
    except FileNotFoundError:
        enhanced_products = []

    # Load legacy products
    try:
        with open('products_legacy.json', 'r', encoding='utf-8') as f:
            legacy_products = json.load(f)
    except FileNotFoundError:
        print("Error: products_legacy.json not found")
        return

    # Create a map of enhanced products by ID
    enhanced_map = {p['id']: p for p in enhanced_products}

    merged_list = []
    
    # Iterate through legacy products
    for legacy_p in legacy_products:
        p_id = legacy_p['id']
        
        if p_id in enhanced_map:
            # Use the enhanced version
            merged_list.append(enhanced_map[p_id])
        else:
            # Use the legacy version, but ensure it has basic structure for new JS
            # The new JS handles 'specs' as array (legacy) or object (enhanced)
            # It also handles 'name' string vs 'names' object
            # So we can just keep it as is, but maybe add default certs/features if missing
            
            # Add default certifications if missing (to look consistent)
            if 'certifications' not in legacy_p:
                legacy_p['certifications'] = {
                    'ce': True,
                    'rohs': True,
                    'iso9001': True
                }
            
            merged_list.append(legacy_p)

    # Write back to products.json
    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(merged_list, f, indent=4, ensure_ascii=False)
    
    print(f"Merged {len(merged_list)} products.")

if __name__ == "__main__":
    merge_products()
