module.exports = {
  title: 'Python programming',
  description: 'Avi Mehenwal python programming practise',
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
    // logo: '/logo4.svg',
    // displayAllHeaders: true,               // Default: false
    activeHeaderLinks: true,
    sidebar: 'auto',
    sidebarDepth: 2,
    searchPlaceholder: 'Search...',
    lastUpdated: 'Last Updated',
    smoothScroll: true,
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Tutorials', link: '/tutorial/' },
      { text: 'Projects', link: '/projects/' }
    ]
  },
  plugins: [
    [ 'vuepress-plugin-mermaidjs', { theme: 'forest'}],
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