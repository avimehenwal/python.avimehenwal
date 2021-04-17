<!-- .vuepress/components/TagList.vue -->
<template>
  <section>
    <button @click="newColor">New Color</button>
    <ul class="flex-container">
      <li v-for="tag in allTags" :key="tag" :style="{background: mycolor}">
        {{ tag }}
      </li>
    </ul>

    <br>
    <h3>website statistics</h3>
    <table class="center">
      <tr>
        <th>Metrics</th>
        <th>Value</th>
      </tr>
      <tr>
        <td>total #pages on site</td>
        <td>{{ allPageCount }}</td>
      </tr>
      <tr>
        <td>total #tags on site</td>
        <td>{{ allTagsCount }}</td>
      </tr>
    </table>

  </section>
</template>

<script>
/** NOTE
 * adding { union } doesnt work
 * Object(...) is not a function
 */
import union from 'lodash.union'

    //- <span v-for="tag in Object.keys(tags)">
    //-   <h2 :id="tag">
    //-     <router-link
    //-       :to="{ path: `/tags.html/#${tag}`}"
    //-       class="header-anchor"
    //-       aria-hidden="true"
    //-     >
    //-     #
    //-     </router-link>
    //-     <Badge vertical="middle" type="tip" :text="tag"/>
    //-   </h2>

    //-   <ul class="w3-ul w3-hoverable">
    //-     <li v-for="page in tags[tag]">
    //-       <router-link :to="{ path: page.path}">
    //-         {{page.title}}
    //-       </router-link>
    //-     </li>
    //-   </ul>
    //- </span>
export default {
  data: () => ({
    mycolor: '#'+(Math.random()*0xFFFFFF<<0).toString(16)
  }),
  mounted () {
    // document.body.style.background = this.mycolor;
  },
  methods: {
    newColor () {
      this.mycolor = '#'+(Math.random()*0xFFFFFF<<0).toString(16);
      // document.body.style.background = this.mycolor;
    },
  },
  computed: {
    allPageCount () {
      return this.$site.pages.length
    },
    allTags () {
      let Tags = []
      this.$site.pages.forEach( (page) => {
        if ('tags' in page.frontmatter) {
          /** NOTE merge 2 arrays in-place
           * 1. using spread operator
           * 2. Array.concat(Array2)
           * Tags.push(...page.frontmatter.tags)
           *
           * FIXME list contains duplicates
           * => lodash _.union([1], [2], [3]) _.uniq([list])
           */
          console.log(page.frontmatter.tags);
          Tags = union(Tags, page.frontmatter.tags)
        }
      })
      return Tags
    },
    allTagsCount () {
      return this.allTags.length
    }
  }
}
</script>

<style lang="stylus" scoped>
$tb=2px       // top-bottm
$rl=10px      // right-left

/** NOTE generate random number for colors
 *
 */
random(min, max)
  return floor( math(0, "random") * max + min )
randomColorChannel()
  return random(0, 255)
randomColor()
  return rgb(randomColorChannel(), randomColorChannel(), randomColorChannel())

section
  text-align: center

.flex-container
  display: flex;
  flex-wrap: wrap
  flex-direction: row;
  justify-content: center

ul.flex-container > li
  background: randomColor();
  margin: 5px;
  padding: $tb $rl ;
  list-style-type: none
  border-radius 15px
  color: #ffffff
  // font-size: 30px;

button
  position: relative;
  display: block;
  margin: 0 auto;
  width: 140px;
  height: 30px;
  border-radius: 30px;
  background: #fff;
  color: #000000;
  border: 1px solid;
  font-weight: bold;
  font-size: 12px;
  cursor: pointer;
  outline: none;

body, button
  -webkit-transition: all 0.4s ease-in-out;
  transition: all 0.4s ease-in-out;

table.center
  margin-left:auto;
  margin-right:auto;
  display: inline-block

</style>