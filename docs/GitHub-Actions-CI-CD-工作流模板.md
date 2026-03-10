# GitHub Actions CI/CD 工作流模板

## 📋 目录
1. [基础 CI 工作流](#基础-ci-工作流)
2. [完整 CD 工作流](#完整-cd-工作流)
3. [团队协作工作流](#团队协作工作流)
4. [自动化标签工作流](#自动化标签工作流)

---

## 🔄 基础 CI 工作流

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          
      - name: Install dependencies
        run: npm ci
        
      - name: Run tests
        run: npm test
        
      - name: Run lint
        run: npm run lint
```

---

## 🚀 完整 CD 工作流

```yaml
# .github/workflows/cd.yml
name: CD

on:
  push:
    tags:
      - 'v*'

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          
      - name: Install dependencies
        run: npm ci
        
      - name: Build
        run: npm run build
        
      - name: Deploy to production
        run: |
          echo "Deploying to production..."
          # Your deployment script here
          
      - name: Create Release
        uses: softprops/action-gh-release@v1
        if: startsWith(github.ref, 'refs/tags/')
        with:
          generate_release_notes: true
```

---

## 🤝 团队协作工作流

```yaml
# .github/workflows/team-collaboration.yml
name: Team Collaboration

on:
  issues:
    types: [opened, labeled, unlabeled]
  pull_request:
    types: [opened, ready_for_review]

jobs:
  notify-team:
    runs-on: ubuntu-latest
    steps:
      - name: Notify team on new issue
        uses: actions/github-script@v7
        if: github.event_name == 'issues'
        with:
          github-token: ${{secrets.GITHUB_TOKEN}}
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: '@team Please review this issue 🙏'
            })
            
      - name: Assign label on PR
        uses: actions/github-script@v7
        if: github.event_name == 'pull_request'
        with:
          github-token: ${{secrets.GITHUB_TOKEN}}
          script: |
            github.rest.issues.addLabels({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              labels: ['review-needed']
            })
```

---

## 🏷️ 自动化标签工作流

```yaml
# .github/workflows/automated-labels.yml
name: Automated Labels

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  label-pr:
    runs-on: ubuntu-latest
    steps:
      - name: Add labels based on files changed
        uses: actions/github-script@v7
        with:
          github-token: ${{secrets.GITHUB_TOKEN}}
          script: |
            const { files } = await github.rest.pulls.listFiles({
              owner: context.repo.owner,
              repo: context.repo.repo,
              pull_number: context.issue.number
            });
            
            const labels = [];
            
            files.forEach(file => {
              if (file.filename.startsWith('src/')) {
                labels.push('src');
              }
              if (file.filename.startsWith('tests/')) {
                labels.push('test');
              }
              if (file.filename.startsWith('docs/')) {
                labels.push('documentation');
              }
            });
            
            if (labels.length > 0) {
              await github.rest.issues.addLabels({
                issue_number: context.issue.number,
                owner: context.repo.owner,
                repo: context.repo.repo,
                labels: labels
              });
            }
```

---

## 📊 实用技巧

### 1. 使用环境变量
```yaml
env:
  NODE_ENV: production
  API_KEY: ${{ secrets.API_KEY }}
```

### 2. 分支保护规则
- requires CI checks
- requires PR review
- prevents force pushes
- requires linear history

### 3. 使用矩阵构建
```yaml
strategy:
  matrix:
    node-version: [16, 18, 20]
    os: [ubuntu-latest, windows-latest]
```

### 4. 缓存依赖
```yaml
- name: Cache node modules
  uses: actions/cache@v4
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-node-
```

---

## 🚀 快速开始

1. 创建 `.github/workflows/` 目录
2. 添加上述工作流文件
3. 提交到仓库
4. 在 Repository Settings → Actions 启用

---

## 📚 参考资源

- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Awesome GitHub Actions](https://github.com/sdras/awesome-actions)
- [GitHub Marketplace](https://github.com/marketplace)

---

*本文档由 AI Agent 创建，基于 GitHub 官方文档整理*