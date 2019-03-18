from app.workers import prepare_text, prepare_img

def test_text():
    result = prepare_text(open('test_data/test_input.html').read())
    expected = open('test_data/output1').read()
    assert expected == result

def test_img():
    result = prepare_img(open('test_data/test_input.html').read())
    expected = open('test_data/output2').read()
    assert expected == result
