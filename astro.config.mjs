import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import rehypeKatex from 'rehype-katex';
import remarkCjkFriendly from 'remark-cjk-friendly/parseOnly';
import remarkCjkFriendlyGfmStrikethrough from 'remark-cjk-friendly-gfm-strikethrough/parseOnly';
import remarkMath from 'remark-math';
import mermaid from 'astro-mermaid';

export default defineConfig({
  site: 'https://agnusdei1207.github.io',
  base: '/study',
  integrations: [
    mermaid({
      theme: 'neutral',
      autoTheme: true,
    }),
    starlight({
      title: 'Tech Notes',
      description: '정보관리기술사·컴퓨터시스템응용기술사 필기 대비 핵심 토픽 학습 노트',
      defaultLocale: 'root',
      locales: {
        root: {
          label: '한국어',
          lang: 'ko',
        },
      },
      sidebar: [
        {
          label: '정보관리기술사 (ITPE)',
          collapsed: false,
          items: [
            {
              autogenerate: {
                directory: 'notes/itpe',
                collapsed: true,
              },
            },
          ],
        },
        {
          label: '컴퓨터시스템응용기술사 (CSAE)',
          collapsed: false,
          items: [
            {
              autogenerate: {
                directory: 'notes/csae',
                collapsed: true,
              },
            },
          ],
        },
        {
          label: '실험 노트 (Lab)',
          collapsed: false,
          items: [
            {
              autogenerate: {
                directory: 'notes/lab',
                collapsed: true,
              },
            },
          ],
        },
      ],
      social: [
        {
          icon: 'github',
          label: 'GitHub',
          href: 'https://github.com/agnusdei1207/study',
        },
      ],
      customCss: ['./src/styles/custom.css'],
      components: {
        PageTitle: './src/components/PageTitle.astro',
        Sidebar: './src/components/Sidebar.astro',
      },
      lastUpdated: true,
      pagefind: false,
      head: [
        { tag: 'script', attrs: { src: '/study/palette-app.js', defer: true } },
        { tag: 'script', attrs: { src: '/study/itpe-glossary-tooltips.js?v=20260926-brr', defer: true } },
      ],
    }),
  ],
  markdown: {
    remarkPlugins: [remarkMath, remarkCjkFriendly, remarkCjkFriendlyGfmStrikethrough],
    rehypePlugins: [rehypeKatex],
  },
});
