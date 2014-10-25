    
def text_field(name, maxlength):
    maxlength = str(maxlength)
    textfield = '<input type="text" name="'+ name + '"  maxlength="' + maxlength + '" size="' + maxlength + '" required>\n'
    return textfield
    
def text_field_not_required(name, maxlength):
    maxlength = str(maxlength)
    textfield = '<input type="text" name="' + name + '" maxlength="' + maxlength + '" size="' + maxlength + '">\n'
    return textfield
    
def dropdown_list(name, items):
    dropdown = '<select name="' + name + '" required>\n'
    for item in items:
        inner_dropdown = '  <option value="' + item + '">' + item + '</option>' + '\n'
        dropdown = dropdown + inner_dropdown
    dropdown = dropdown + '</select>\n'
    return dropdown

def file_field(name):
    return '<input type="file" name="' + name + '"/>'

collection_status = ['Permanent', 'Temporary']
item_classification = [
                        'Bodice/Blouse', 'Skirt', 'Dress', 'Pants', 'Suit Pants',
                        'Suit Dress', 'Suit Skirt', 'Coat', 'Jacket', 'Cape',
                        'Shawl', 'Scarf', 'Bathing Suit', 'Underwear', 'Shirt'
                      ]
for_whom = ['Men', 'Boys', 'Women', 'Girls', 'Children-Infants', 'Children-Toddlers']



if __name__ == '__main__':
    print dropdown_list('collection', collection_status)
    print text_field('res', 5)
    print dropdown_list('item_class', item_classification)
    print text_field_not_required('image_url', 10)
    print file_field('img')
