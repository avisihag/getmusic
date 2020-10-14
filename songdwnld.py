from requests_html import HTMLSession
import webbrowser


def ytlink(t):
    '+'.join(t.split())
    session = HTMLSession()
    search_page = session.get(
        'https://www.youtube.com/results?search_query=' + t)
    html = search_page.html
    html.render()  # if it gives a timeout just do it again, you'll figure that out
    all_vids = html.find('#thumbnail')
    first_vid = all_vids[0]
    link_first_vid = first_vid.attrs['href']

    return str('https://www.youtube.com' + link_first_vid)
