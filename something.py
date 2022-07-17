def transform(img_tag):

    split_tag = img_tag.split("'")

    img_path = split_tag[1]
    img_alt = split_tag[3]

    new_tag = f'![{img_alt}]({img_path})'
    print(new_tag)


image_tag = "<img src='assets/images/wireframes/wf-desktop-mp2' alt='desktop wireframe'>"

transform(image_tag)