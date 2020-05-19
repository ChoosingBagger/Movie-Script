class Template(object):
    def generateTemplate(
        thread_movie_title, director, imgLink, imdb_link, tmdb_link, rt_link,
        bluray_link, plot_summary, file_name, movie_distributor, country,
        imdb_year, movie_title, bbcode
    ):
        source = 'TBD'
        if args.source:
            source = args.source
        logs = '[*][b]Logs:[/b]\n[spoiler][align=left]LOGS[/align][/spoiler]'
        if args.dgdemux:
            logs = ''
        template = f"""\n[quote][align=center][size=7][b]{thread_movie_title}[/b][/size]
    [size=5]by {director}[/size][/align][/quote]
    [align=center][img]{imgLink}[/img][/align]
    [align=center][quote][size=4][b][url={imdb_link}][color=#f3e800]IMDb[/color][/url] | [url={tmdb_link}][color=#008b46]TheMovieDB[/color][/url] | [url={rt_link}][color=#BF0000]Rotten[/color][/url] | [url={bluray_link}][color=#00468b]BluRay[/color][/url] | [url=https://awesome-hd.me/forums.php?action=viewthread&threadid=#####][color=#6A0DAD]Discuss[/color][/url][/b][/size][/quote][/align]
    [align=center][size=3][b][color=#8b0000]Plot[/color][/b][/size][quote]{plot_summary}[/quote][/align]
    [align=center][size=3][b][color=#8b0000]Remux Information[/color][/b][/align][quote][*][b]Name: [/b]{file_name}
    [*][b]Source: [/b]{source}
    [*][b]Edition: [/b]{movie_distributor} | {country}
    [*][b]Video: [/b]TBD
    [*][b]Audio: [/b]TBD
    [*][b]Subtitles: [/b]TBD
    [*][b]Chapters: [/b]Included (TBD)[/quote]
    [align=center][size=3][b][color=#8b0000]Notes[/color][/b][/align][quote]TBD[/quote]
    [align=center][size=3][b][color=#8b0000]Additional Information[/color][/b][/size][/align][quote][*][b]BDInfo:[/b]
    [spoiler][align=left]BDINFO[/align][/spoiler]{logs}[*][b]Mediainfo:[/b]
    [spoiler][align=left]MEDIAINFO[/align][/spoiler][/quote]
    [align=center][size=3][b][color=#8b0000]Screenshots[/color][/b][/size][/align]
    [align=center][spoiler]{bbcode}[/spoiler][/align]"""
