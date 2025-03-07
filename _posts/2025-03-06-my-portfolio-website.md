---
layout: post
title: "나만의 포트폴리오 웹사이트 만들기"
date: 2025-03-06 02:20:29
categories: [웹사이트, 포트폴리오]
tags: [Jekyll, 블로그, 웹 개발, 포트폴리오]
---

# 나만의 포트폴리오 웹사이트 만들기

나만의 포트폴리오 웹사이트를 만드는 것은 오늘날 극히 중요한 작업입니다. 좋은 포트폴리오는 여러분의 기술, 경험, 그리고 창의력을 보여주는 중요한 도구가 될 수 있습니다. 특히, Jekyll과 같은 정적 사이트 생성기를 사용하여 수월하게 구축할 수 있습니다. 이번 글에서는 Jekyll을 활용하여 어떻게 나만의 포트폴리오 웹사이트를 만들어가는지에 대해 상세히 알아보겠습니다.

## 포트폴리오 웹사이트의 중요성

포트폴리오 웹사이트는 여러분의 전문성을 증명하고, 네트워킹의 기회를 넓힐 수 있는 훌륭한 수단이 됩니다. 특히 디지털 디자인, 개발, 콘텐츠 제작 등의 분야에서 일하는 분들에게 필수입니다. 포트폴리오를 통해 잠재 고객이나 고용주에게 자신의 작업을 직접적으로 보여줄 수 있습니다.

### 포트폴리오 웹사이트에 포함해야 할 요소들

포트폴리오 웹사이트를 만들 때, 전시하고자 하는 작품 외에도 다음과 같은 요소들을 고려해야 합니다.

1. **소개(About)**: 자신에 대한 간단한 소개와 경력, 전문 기술을 포함하세요.
2. **작품 갤러리(Work Gallery)**: 과거에 작업했던 프로젝트들을 나열하고, 각 프로젝트에 대한 설명과 함께 이미지를 포함하세요.
3. **연락처(Contact)**: 방문자가 쉽게 당신에게 연락할 수 있도록 이메일, SNS 링크 등을 제공하세요.
4. **이력서 또는 경력(Resume/CV)**: 이력서 페이지를 만들어 자신의 학력과 경력을 자세히 명시하세요.
5. **블로그(Blog)**: 자신의 생각이나 작업 프로세스를 공유하는 블로그 항목을 추가하면 개인 브랜드를 구축하는 데 큰 도움이 됩니다.

## Jekyll 소개

Jekyll은 Ruby로 작성된 정적 사이트 생성기로, GitHub Pages와 쉽게 연동되어 사용될 수 있으며, 블로그나 포트폴리오 웹사이트를 만드는 데 최적화되어 있습니다. Jekyll은 Markdown을 지원하고, 다양한 플러그인과 테마를 통해 자신만의 스타일을 쉽게 적용할 수 있는 장점이 있습니다.

### Jekyll 설치하기

Jekyll 설치를 위해서는 Ruby가 설치되어 있어야 합니다. 아래의 명령어를 사용하여 Jekyll과 Bundler를 설치할 수 있습니다.

```bash
gem install --user-install bundler jekyll
```

그 후, 새로운 Jekyll 프로젝트를 생성하려면 아래와 같은 명령어를 사용할 수 있습니다.

```bash
jekyll new my-portfolio
cd my-portfolio
bundle exec jekyll serve
```

이 명령어는 새로운 Jekyll 웹사이트를 생성하고, 웹서버를 시작하여 `http://localhost:4000`에서 확인할 수 있게 해줍니다.

## 나만의 포트폴리오 만들기

이제 Jekyll을 이용해 포트폴리오 웹사이트를 만들 준비가 되었습니다. 다음 단계는 본격적인 웹사이트의 내용을 작성하는 것입니다.

### 1. `_config.yml` 설정하기

Jekyll 프로젝트의 루트 디렉토리에 있는 `_config.yml` 파일을 열어 사이트의 기본 정보를 입력합니다. 예를 들어,

```yaml
title: 나만의 포트폴리오
email: example@example.com
description: 나의 웹 포트폴리오입니다.
copyright: '2025 Your Name'
```

### 2. 페이지 추가하기

Jekyll는 `_posts`, `_pages`와 같은 디렉토리를 통해 페이지를 관리합니다. 포트폴리오의 각 섹션에 대한 Markdown 파일을 생성하여 내용을 추가합니다. 예를 들어 `about.md` 파일을 아래와 같이 작성할 수 있습니다.

```markdown
---
title: "About Me"
date: 2025-03-06
layout: page
---

# 나에 대한 소개

저는 웹 개발자이자 디자이너이며, 다양한 프로젝트를 진행해왔습니다. 제 작업은 주로 사용자 경험(UX)과 인터페이스(UI) 디자인에 초점을 맞추고 있습니다.  

이곳에 제 경험과 기술을 확인해보세요!
```

### 3. 테마 선택하기

디자인을 더욱 멋지게 보이게 하기 위해 Jekyll 테마를 선택할 수 있습니다. [Jekyll Themes](https://jekyllthemes.org/) 웹사이트에서 여러 가지 테마를 확인하고, 다운로드하여 `_layouts` 디렉토리에 추가합니다.

### 4. 프로젝트 갤러리 만들기

포트폴리오의 핵심은 자신의 작업입니다. 각 프로젝트에 대한 Markdown 파일을 생성하고, 이미지 파일을 `assets/images` 디렉토리에 업로드하여 연결할 수 있습니다. 예를 들어 `project1.md`와 같은 파일을 만들고 다음과 같이 작성할 수 있습니다.

```markdown
---
title: "프로젝트 1"
date: 2025-03-06
layout: project
---

# 프로젝트 1: 웹사이트 디자인

![프로젝트 1 이미지](../assets/images/project1.png)

이 프로젝트는 XYZ 클라이언트를 위해 디자인한 웹사이트입니다. 사용자 친화적인 인터페이스를 제공하기 위해 많은 연구와 디자인 샘플이 포함되었습니다.
```

## 배포하기

모든 페이지 작성이 완료되면 이제 웹사이트를 배포할 차례입니다. GitHub Pages를 통해 무료로 호스팅할 수 있으며, Ваш проект의 `main` 브랜치에 푸시하면 자동으로 배포됩니다.

1. GitHub에 새로운 리포지토리를 생성합니다.
2. 프로젝트 파일을 그 리포지토리에 푸시합니다.
3. GitHub Pages 설정을 활성화하여 `main` 브랜치의 `root`를 선택합니다.

## 결론

나만의 포트폴리오 웹사이트를 만드는 것은 간단하면서도 흥미로운 과정입니다. Jekyll을 통해 쉽게 웹사이트를 구축하고 유지관리할 수 있으며, 창의력을 발휘할 수 있는 기회를 제공합니다. 이 글이 여러분께 도움이 되길 바랍니다. 이제 여러분의 멋진 포트폴리오 웹사이트를 만들어 보세요!