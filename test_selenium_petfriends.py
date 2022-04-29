import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome(r'C:\Users\HP\PycharmProjects\chromedriver.exe')
    pytest.driver.get('https://petfriends1.herokuapp.com/login')
    yield
    pytest.driver.quit()


def test_all_pets():
    pytest.driver.implicitly_wait(10)
    pytest.driver.find_element_by_id('email').send_keys('marinatest@1secmail.com')
    pytest.driver.find_element_by_id('pass').send_keys('testtest')
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    assert pytest.driver.find_element_by_tag_name('h1').text == 'PetFriends'

    images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
    descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != '', 'There is pet without photo'
        assert names[i].text == '', 'There is pet without name'
        assert descriptions[i].text != '', 'There is pet without type and age'
        assert ',' in descriptions[i].text
        parts = descriptions[i].text.split(',')
        assert len(parts[0]) > 0, 'There is pet without type'
        assert len(parts[1]) > 0, 'There is pet without age'


def test_show_my_pets():
    pytest.driver.find_element_by_id('email').send_keys('marinatest@1secmail.com')
    pytest.driver.find_element_by_id('pass').send_keys('testtest')
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    pytest.driver.find_element_by_link_text(u'Мои питомцы').click()

    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.\\.col-sm-4.left')))
    stat = pytest.driver.find_elements_by_css_selector('.\\.col-sm-4.left')
    count = stat[0].text.split('\n')
    count = count[1].split(' ')
    count = int(count[1])

    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'all_my_pets')))
    images = pytest.driver.find_elements_by_css_selector('.table.table-hover img')
    pets = pytest.driver.find_elements_by_css_selector('.table.table-hover tbody tr td')
    # проверяем, что кол-во питомцев совпадает с данными статистики
    assert len(pets) == count * 4

    s = 0
    names = []
    an_types = []
    ages = []

    for i in range(count):
        if images[i].get_attribute('src') == '':
            s += 1
        name = pets[i*4]
        an_type = pets[i*4+1]
        age = pets[i*4+2]
        names.append(name.text)
        an_types.append(an_type.text)
        ages.append(age.text)
    # проверяем, что у всех питомцев есть имя, вид, возраст
        assert name.text != '', 'There is pet without name'
        assert an_type.text != '', 'There is pet without type'
        assert age.text != '', 'There is pet without age'

    # проверяем, что питомцев без фото не больше половины
    assert s <= count//2, "More than a half of pets have no photo"

    # проверяем, что нет одинаковых имен
    names_set = set(names)
    assert len(names_set) == count, 'There are some pets with the same names'

    # проверяем, что нет одинаковых питомцев
    same_pets = False
    if len(names_set) < count:
        for i in range(len(names)-1):
            for j in range(i+1, len(names)):
                if (names[i] == names[j]) and (an_types[i] == an_types[j]) and (ages[i] == ages[j]):
                    same_pets = True
        assert same_pets is False, 'There are the same pets'
