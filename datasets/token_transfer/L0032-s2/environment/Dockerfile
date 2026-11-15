FROM ubuntu:24.04

# Pre-install what Harbor's opencode agent installs at setup (same nvm, Node and opencode
# versions), so per-trial setup takes seconds. terminus-2 ignores all of this.
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates nodejs npm coreutils \
    && rm -rf /var/lib/apt/lists/*
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.2/install.sh | env -u NODE_VERSION bash \
    && export NVM_DIR="$HOME/.nvm" && . "$NVM_DIR/nvm.sh" \
    && nvm install 22 && nvm alias default 22 && npm i -g opencode-ai@1.19.5 && opencode --version

WORKDIR /app
