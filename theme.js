/* ============================================================
   Primer deck — design tokens (the palette + type).
   This is the single source of truth for COLOR and FONT.
   Every slide links this file right after the Tailwind CDN
   script, so `bg-bgdark`, `text-teal`, `font-serif`, etc.
   resolve the same way everywhere. Change a brand color here
   once and every slide follows. Structure lives in deck.css.
   ============================================================ */
tailwind.config = {
  theme: { extend: {
    colors: {
      ink:'#1A1A1A', ink2:'#1D1D1D',
      bgdark:'#193C33', bgdark2:'#1A3C34',
      paper:'#FBFDFB',
      teal:'#2C8B7B', teal2:'#2D8B7A', tealbar:'#408179',
      tint:'#E6F6F3', tint2:'#E6F7F3',
      body:'#3D4F47', muted:'#6B7D75', gray2:'#5A5A5A',
      line:'#D8DDD9',
      risk:'#C0392B', riskbg:'#FBEEEC', riskline:'#D64C42',
      warn:'#B7791F', okdot:'#2C8B7B', subj:'#E07A3E',
    },
    fontFamily: {
      serif:['"Playfair Display"','Georgia','serif'],
      sans:['Inter','system-ui','sans-serif'],
      mono:['ui-monospace','SFMono-Regular','Menlo','monospace'],
    },
  } },
};
