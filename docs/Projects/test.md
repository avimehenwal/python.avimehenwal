# 1. Test Page

<Badge type="tip" vertical="top" text="beta+"  />
<Badge type="warning" vertical="top" text="beta+"  />
<Badge type="error" vertical="top" text="beta+"  />


## 1.1. markdown-it-ins

++inserted++

## 1.2. markdown-it-mark

==marked==

### 1.2.1. sub

H~2~0 H~2~

### 1.2.2. Sup

29^th^   s^e^c~o~n^d^

## 1.3. Footnote

Here is a footnote reference,[^1] and another.[^longnote]

[^1]: Here is the footnote.

[^longnote]: Here's one with multiple blocks.

## 1.4. Definition List

Term 1

: Definition 1

Term 2 with *inline markup*

:   Definition 2

        { some code, part of Definition 2 }

    Third paragraph of definition 2.

## 1.5. Abbr

*[HTML]: Hyper Text Markup Language
*[W3C]:  World Wide Web Consortium
The HTML specification
is maintained by the W3C.

## 1.6. Emoji

:smile: :tada: :100:


## 1.7. Container

::: warning
*here be dragons*
:::

::: tip
tip tip tip tip tip tip tip tip tip tip tip
:::

::: danger
error error error error error error error error
:::

::: quote alexander
Some quote please
:::

::: quote
Some quote without header
:::


::: theorem Newton's First Law
In an inertial frame of reference, an object either remains at rest or continues to move at a constant velocity, unless acted upon by a force.

  ::: right
  From [Wikipedia](https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion)
  :::
:::

::: tip
Tip container of `@vuepress/theme-default`
:::

::: right
From [Wikipedia](https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion)
:::

## 1.8. Inserting code snipped from a python file

<<< @/../src/hidden_features.py#snippet{5}


## 1.10. Badges

sadnfoidsnofsd  klsndfi nsidfon siodnf dsf
<Badge type="warning" vertical="top" text="Lazy loading"  />
isdbfios nfosdnf osdn fosnf osndfion siodnfosdn
<Badge type="warning" vertical="middle" text="Lazy loading"  />
sndofkn odsnfios ndfioksnd iofnsiodfnios nfio
<Badge type="tip" vertical="middle" text="Lazy loading"  />
sndofkn odsnfios ndfioksnd iofnsiodfnios nfio
<Badge type="error" vertical="middle" text="Lazy loading"  />
dsifnioa fnioasnf ionadsio fniodfn oidn f

## 1.11. Mermaid

### 1.11.1. Sequence Diagram

``` mermaid
sequenceDiagram
Alice->John: Hello John, how are you?
loop every minute
    John-->Alice: Great!
end
```

### 1.11.2. Pie Chart

```mermaid
pie title Pets adopted by volunteers
	"Dogs" : 386
	"Cats" : 85
	"Rats" : 15
```

### 1.11.3. Git graph

```mermaid
gitGraph:
options
{
    "nodeSpacing": 100,
    "nodeRadius": 10
}
end
commit
branch newbranch
checkout newbranch
commit
commit
checkout master
commit
commit
merge newbranch
```

### 1.11.4. Gantt Chart

[Basics of Gantt Chart](https://avimehenwal.in/blog/gantt-chart/)

```mermaid
gantt
dateFormat  YYYY-MM-DD
title Adding GANTT diagram to mermaid
excludes weekdays 2014-01-10

section Sample Project A
Completed task            :done,    des1, 2014-01-06,2014-01-08
Active task               :active,  des2, 2014-01-09, 3d
Future task               :         des3, after des2, 5d
Future task2              :         des4, after des3, 5d

section Critical tasks
Completed task in the critical line :crit, done, 2014-01-06,24h
Implement parser and jison          :crit, done, after des1, 2d
Create tests for parser             :crit, active, 3d
Future task in critical line        :crit, 5d
Create tests for renderer           :2d
Add to mermaid                      :1d

section Documentation
Describe gantt syntax               :active, a1, after des1, 3d
Add gantt diagram to demo page      :after a1  , 20h
Add another diagram to demo page    :doc1, after a1  , 48h

section Last section
Describe gantt syntax               :after doc1, 3d
Add gantt diagram to demo page      :20h
Add another diagram to demo page    :48h
```


### 1.11.5. Add all markdown packages

```
yarn add -D vuepress-plugin-container vuepress-plugin-mathjax vuepress-plugin-mermaidjs \
    @vuepress/plugin-nprogress vuepress-plugin-auto-sidebar @vuepress/plugin-back-to-top \
    @vuepress/plugin-blog @vuepress/plugin-medium-zoom @vuepress/plugin-last-updated \
    @vuepress/plugin-active-header-links @vuepress/plugin-google-analytics vuepress-plugin-git-log \
    @vuepress/plugin-pwa @dovyp/vuepress-plugin-clipboard-copy vuepress-plugin-reading-time \
    vuepress-plugin-img-lazy vuepress-plugin-social-share vuepress-plugin-reading-progress \
    markdown-it-container markdown-it-footnote markdown-it-deflist markdown-it-emoji \
    markdown-it-mark markdown-it-abbr markdown-it-sub markdown-it-sup markdown-it-ins \
    markdown-it-imsize markdown-it-todo

yarn add vuepress-plugin-reading-progress
```
