module.exports = {
  title: 'Programming',
  description: 'Avi Mehenwal python programming practise',
  head: [
    ['link', { rel: 'icon', href: '/favicon.ico' }]
  ],
  configureWebpack: {
    resolve: {
      alias: {
        '@sc': 'screenshots'
      }
    }
  },
  themeConfig: {
    author: 'avimehenwal',
    repo: 'avimehenwal/python.avimehenwal',
    repoLabel: 'GitHub',
    editLinks: true,
    editLinkText: 'Help me improve this page!',
    logo: '/logo.svg',
    // displayAllHeaders: true,               // Default: false
    activeHeaderLinks: true,
    sidebar: 'auto',
    sidebarDepth: 2,
    searchPlaceholder: 'Search...',
    lastUpdated: 'Last Updated',
    smoothScroll: true,
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Tags', link: '/tags' },
      { text: 'Tutorials', link: '/tutorials/' },
      { text: 'Projects', link: '/projects/' }
    ]
  },
  plugins: [
    "@vuepress/plugin-active-header-links",
    "@vuepress/plugin-last-updated",
    "@vuepress/plugin-medium-zoom",
    "@vuepress/plugin-back-to-top",
    "vuepress-plugin-auto-sidebar",
    "@vuepress/plugin-nprogress",
    "@vuepress/plugin-blog",
    "@vuepress/pwa",
    // https://mermaid-js.github.io/mermaid/#/mermaidAPI?id=mermaidapi-configuration-defaults
    [ 'vuepress-plugin-mermaidjs', {
      // "theme": 'forest',
      // "theme": 'dark',
      "theme": "default",
      // "font-size": "20",
      gantt: {
        titleTopMargin:20,
        barHeight:30,
        barGap:10,
        topPadding:50,
        leftPadding:0,
        gridLineStartPadding:10,
        fontSize:25,
        fontFamily:'"Open-Sans", "sans-serif"',
        numberSectionStyles:4,
        axisFormat:'%Y-%m-%d',
      }
    }],
    [
      'vuepress-plugin-mathjax',
      {
        target: 'svg',
        macros: {
          '*': '\\times',
        },
      },
    ],
    [ 'vuepress-plugin-git-log' ],
    [ '@vuepress/google-analytics', { 'ga': process.env.GA } ],
    [
      'vuepress-plugin-container',
      {
        type: 'right',
        defaultTitle: '',
      },
    ],
    [
      'vuepress-plugin-container',
      {
        type: 'theorem',
        before: info => `<div class="theorem"><p class="title">${info}</p>`,
        after: '</div>',
      },
    ],
    [ // DOESNT WORK, want to put title(author name) after main content
      'vuepress-plugin-container',
      {
        type: 'quote',
        defaultTitle: 'Anonymous',
        before: info => `<div class="quote">`,
        after: info => `<p class="title">${info}</p></div>`,
      },
    ]
  ],
  markdown: {
    // options for markdown-it-anchor
    // anchor: { permalink: false },
    // options for markdown-it-toc
    // toc: { includeLevel: [1, 2] },
    linkify: true,                // convert markdown link texts to links
    extendMarkdown: md => {
      md.use(require('markdown-it-container'))
      md.use(require('markdown-it-footnote'))
      md.use(require('markdown-it-deflist'))
      md.use(require('markdown-it-emoji'))
      md.use(require('markdown-it-abbr'))
      md.use(require('markdown-it-mark'))
      md.use(require('markdown-it-sup'))
      md.use(require('markdown-it-sub'))
      md.use(require('markdown-it-ins'))
    }
  }
}

// https://github.com/avimehenwal/avimehenwal2/blob/master/content/.vuepress/config.js