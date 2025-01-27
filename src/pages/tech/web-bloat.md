---
title: The Web is Bloated
created: 2024-12-17
---

## The issue

- The Web is bloated - most of the Web is static content and should be blazing fast... but is not.
- Many people worldwide do not have high speed Internet.
- Issue best summarized [here](https://idlewords.com/talks/website_obesity.htm#crisis).

## Solutions

- Most websites do not need to manage state and deliver static content :
  - Use a static webpage framework like [hugo](https://gohugo.io/).
  - Avoid WordPress(r).
  - Drastically reduce your images / videos : compress, resize, ...
  - Host your website closed to your customers.
- Always test your code / website in degraded mode first and assume this is the main execution flow of the app.
- [Anybrowser : make your website work for everyone](https://anybrowser.org/campaign/)
- [Proper Design advices](https://www.w3.org/DesignIssues/Principles.html)
- [Use Responsive images if dealing with big images](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)
- [Avoid unnecessary data transfers](https://github.com/fireship-io/flamethrower)
- [Content-first web](https://speakerdeck.com/brad_frost/for-a-future-friendly-web)
- [Hardcore : use Gemini or Gopher instead of the Web](https://gemini.circumlunar.space/)

# Ressources

- [Conseils de sobriété numérique Web (FR)](https://awebsome.fr/blog-awebsome/)
- [The Web obesity](https://idlewords.com/talks/website_obesity.htm)
- [An history of Web bloat](https://danluu.com/web-bloat/)
- [Compute your website bloat score](https://www.webbloatscore.com/)
- [About the carbon footprint of the Web](https://dannyvankooten.com/website-carbon-emissions/)
- [Compute the carbon footprint of your website](https://www.websitecarbon.com)
- [Tim Berners-Lee (inventor of the World Wide Web) website : a non-bloat example](https://www.w3.org/People/Berners-Lee/)
