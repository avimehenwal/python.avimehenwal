<!-- .vuepress/components/TagList.vue -->
<template lang="html">
  <div>
    <h1>
      Tags <Badge type="warning" :text="tagcount"/>
    </h1>

    <span v-for="tag in Object.keys(tags)">
      <h2 :id="tag">
        <router-link
          :to="{ path: `/tags.html/#${tag}`}"
          class="header-anchor"
          aria-hidden="true"
        >
        #
        </router-link>
        <Badge vertical="middle" type="tip" :text="tag"/>
        <Badge type="error" :text="tags[tag].length"/>
        <!-- <Badge type="warning" :text="tags[tag].length"/> -->
      </h2>

      <ul class="w3-ul w3-hoverable">
        <li v-for="page in tags[tag]">
          <router-link :to="{ path: page.path}">
            {{page.title}}
          </router-link>
        </li>
      </ul>
    </span>
  </div>
</template>

<script>
export default {
  // data () {
  //   return {
  //     dtags: this.tags[tag]
  //   }
  // },
  computed: {
    tags() {
      let tags = {}
      for (let page of this.$site.pages) {
        for (let index in page.frontmatter.tags) {
          const tag = page.frontmatter.tags[index]
          if (tag in tags) {
            tags[tag].push(page)
          } else {
            tags[tag] = [page]
          }
        }
      }
      return tags
    },
    tagcount () {
      return Object.keys(this.tags).length;
    }
  }
}
</script>