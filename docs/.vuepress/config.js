module.exports = {
  title: 'Python programming',
  description: 'avi mehenwal python programming practise',
  configureWebpack: {
    resolve: {
      alias: {
        '@sc': 'screenshots'
      }
    }
  },
  markdown: {
    // options for markdown-it-anchor
    // anchor: { permalink: false },
    // options for markdown-it-toc
    // toc: { includeLevel: [1, 2] },
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