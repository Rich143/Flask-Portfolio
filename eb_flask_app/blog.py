import codecs
import os


# This function takes a directory, then constructs a dict with all of the relevant blog post info
# for every single markdown file within that directory.
def construct_blog_posts(path):
    if not os.path.exists(path):
        return []

    def chomp_md(title):
        return title.replace(".md", "")

    def construct_post_id(counter):
        return 'blog_post_' + str(counter)

    blog_posts = []
    filenames = os.listdir(path)

    if '.DS_Store' in filenames:
        filenames.remove('.DS_Store')

    post_id_counter = 1

    for post in filenames:
        name = chomp_md(post)
        split_filename = post.split('-')

        post_info = {}
        post_info['date'] = '-'.join(split_filename[:3])
        post_info['title'] = name.replace(post_info['date'] + '-', '')
        post_info['id'] = construct_post_id(post_id_counter)

        with codecs.open(path + post, 'r', encoding='utf-8') as f:
            post_info['text'] = f.read()

        blog_posts.append(post_info)
        post_id_counter += 1

    return reversed(sorted(blog_posts))

if __name__ == '__main__':
    print [(post['title'], post['id']) for post in construct_blog_posts('static/assets/posts/')]
