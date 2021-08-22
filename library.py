def get_info(driver, id):
    info = []
    home_window = driver.window_handles[0]
    window_i = driver.window_handles[1]
    driver.switch_to_window(window_i)

    height = driver.execute_script("return document.body.scrollHeight") - 200

    for item in range (0, height, 50):
        driver.execute_script(f"window.scrollTo(0, {item})")

        name = driver.find_element_by_css_selector('.title-info-title-text').text
        price = driver.find_element_by_css_selector('.item-price-wrapper').text
        el_date = driver.find_element_by_css_selector('.title-info-metadata-item-redesign').text
        tel_number = driver.find_element_by_css_selector('.price-value-string js-price-value-string').text
        kompany = driver.find_element_by_css_selector('.seller-info-value').text
        user_name = driver.find_element_by_css_selector('.seller-info-name.js-seller-info-name').text
        number = driver.find_element_by_css_selector('.item-view-search-info-redesign > span').text

        viewed = driver.find_element_by_css_selector('.title-info-metadata-item.title-info-metadata-views').text
        address = driver.find_element_by_css_selector('.item-address__string').text
        description = driver.find_element_by_css_selector('.item-description').text
    
    # print(number)
    el_info = {
        'id': id,
        'name': name,
        'price': price,
        'date': el_date,
        'kompany': kompany,
        'user_name': user_name,
        # 'number': number,
        'viewed': viewed,
        'address': address,
        'description': description
    }
    info.append(el_info)

    return info
    driver.close()
    driver.switch_to_window(home_window)