<template>
<div>
  <!-- Top Panel / Banner -->
  <!-- <div class="w3-panel w3-display-container w3-animate-top">
    <span onclick="this.parentElement.style.display='none'"
    class="w3-button w3-large w3-display-topright">&times;</span>
    <h3>
      <i class="fa fa-search"></i>
      {{ this.$page.title }}
    </h3>
    <p>
      <Badge vertical="middle" type="tip" :text="pageCount"/> Articles
    </p>
  </div> -->

  <!-- List Article Data -->
  <!-- <ul class="w3-ul w3-card">
    <div class="w3-animate-bottom" v-for="page in pages">
      <li class="w3-bar">
        <span onclick="this.parentElement.style.display='none'" class="w3-bar-item w3-button w3-white w3-xlarge w3-right">×</span>
        <router-link  :to="page.path">
          <img src="/logo4.svg" class="w3-bar-item w3-hide-small" style="width:100px">
          <div class="w3-bar-item">
            <span class="w3-large w3-xlarge">
              {{ page.title }}
            </span><br>
            <span v-for="tag in page.frontmatter.tags" style="margin-right:5px;">
              <router-link
                :to="{ path: `/tags.html#${tag}`}"
              >
                <Badge type="warning" text="tag"/>
              </router-link>
            </span>
          </div>
        </router-link>
      </li>
    </div>
  </ul> -->

  <ol>
  <div v-for="page in pages">
    <li>
      <a :href="page.regularPath">
        <h3>
          {{ page.title }}
        </h3>
      </a>
    </li>
  </div>
  </ol>

</div>
</template>

<script>
export default {
  data() {
    return {
      pages: [],
    }
  },
  mounted() {
    this.$site.pages.forEach(page => {
      if (page.path !=this.currentPath && page.path.includes(this.currentPath)) {
        this.pages.push(page)
      }
    })
  },
  computed: {
    pageCount () {
      return this.pages.length.toString()
    },
    currentPath () {
      return this.$page.path
    }
  }
}
</script>

<style scoped>

ol {
  max-width: 350px;
  counter-reset: my-awesome-counter;
  list-style: none;
  padding-left: 40px;
}
ol li {
  margin: 0 0 0.5rem 0;
  counter-increment: my-awesome-counter;
  position: relative;
}
ol li::before {
  content: counter(my-awesome-counter);
  color: #306998;
  font-size: 1.5rem;
  font-weight: bold;
  position: absolute;
  --size: 32px;
  left: calc(-1 * var(--size) - 10px);
  line-height: var(--size);
  width: var(--size);
  height: var(--size);
  top: 0;
  transform: rotate(-10deg);
  background: lightgrey;
  border-radius: 50%;
  text-align: center;
  box-shadow: 3px 5px 0 #999;
}

</style>