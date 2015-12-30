import codecs
from os import listdir


# This function takes a directory, then constructs a dict with all of the relevant blog post info
# for every single markdown file within that directory.
def construct_blog_posts(path):
    def chomp_md(title):
        return title.replace(".md", "")

    blog_posts = []
    filenames = listdir(path)

    if '.DS_Store' in filenames:
        filenames.remove('.DS_Store')

    for post in filenames:
        split_filename = chomp_md(post).split('-')

        post_info = {}
        post_info['date'] = '-'.join(split_filename[:3])
        post_info['title'] = ' '.join(split_filename[3:])

        with codecs.open(path + post, 'r', encoding='utf-8') as f:
            post_info['text'] = f.read()

        blog_posts.append(post_info)

    return blog_posts

if __name__ == '__main__':
    print construct_blog_posts('static/assets/posts/')
