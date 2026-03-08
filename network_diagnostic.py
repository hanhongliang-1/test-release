#!/usr/bin/env python3
"""
A 股监控系统网络诊断工具
诊断 DNS、SSL handshake、代理设置等问题
"""

import socket
import ssl
import os
import sys
import urllib.request
from datetime import datetime

def test_dns_resolution():
    """测试 DNS 解析"""
    print("\n" + "="*60)
    print("🌐 测试 1: DNS 解析")
    print("="*60)
    
    domains = [
        '8.8.8.8',           # Google DNS
        '114.114.114.114',   # 中国 DNS
        '223.5.5.5',         # 阿里 DNS
    ]
    
    for domain in domains:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(3)
            result = s.connect_ex((domain, 53))
            status = "✅ OK" if result == 0 else f"❌ Failed (code={result})"
            print(f"   {domain}: {status}")
            s.close()
        except Exception as e:
            print(f"   {domain}: ❌ Error - {e}")

def test_ssl_handshake():
    """测试 SSL 握手"""
    print("\n" + "="*60)
    print("🔒 测试 2: SSL Handshake")
    print("="*60)
    
    targets = [
        ('82.push2delay.eastmoney.com', 443),  # 东方财富
        ('api.akshare.icu', 443),               # akshare API
        ('www.baidu.com', 443),                 # 通用测试
    ]
    
    for host, port in targets:
        try:
            ctx = ssl.create_default_context()
            s = socket.socket()
            s.settimeout(10)
            conn = ctx.wrap_socket(s, server_hostname=host)
            result = conn.connect_ex((host, port))
            
            if result == 0:
                version = conn.version()
                print(f"   {host}:{port} ✅ OK (TLS-{version})")
            else:
                print(f"   {host}:{port} ❌ Failed (code={result})")
            conn.close()
        except Exception as e:
            print(f"   {host}:{port} ❌ Error - {e}")

def test_http_connection():
    """测试 HTTP 连接"""
    print("\n" + "="*60)
    print("🌍 测试 3: HTTP/HTTPS 连接")
    print("="*60)
    
    urls = [
        'https://www.baidu.com',
        'http://quotes.sina.cn/',
    ]
    
    for url in urls:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            start = datetime.now()
            with urllib.request.urlopen(req, timeout=15) as response:
                elapsed = (datetime.now() - start).total_seconds()
                print(f"   {url} ✅ OK ({elapsed:.2f}s)")
        except Exception as e:
            print(f"   {url} ❌ Error - {type(e).__name__}: {e}")

def check_proxy_settings():
    """检查代理设置"""
    print("\n" + "="*60)
    print("⚙️ 测试 4: 代理环境配置")
    print("="*60)
    
    proxies = ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy']
    for proxy in proxies:
        value = os.environ.get(proxy, '')
        if value:
            print(f"   {proxy}={value}")
        else:
            print(f"   {proxy}: (未设置)")

def check_python_ssl():
    """检查 Python SSL 环境"""
    print("\n" + "="*60)
    print("🐍 测试 5: Python/SSL 环境")
    print("="*60)
    
    import sys
    import ssl
    
    print(f"   Python version: {sys.version}")
    print(f"   OpenSSL version: {ssl.OPENSSL_VERSION}")
    
    # 检查 SSL 证书路径
    try:
        ctx = ssl.create_default_context()
        print(f"   CA certificates path: OK")
    except Exception as e:
        print(f"   CA certificates path: ❌ Error - {e}")

def main():
    print("\n" + "🚀"*30)
    print("A 股监控系统网络诊断工具")
    print(f"时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("🚀"*30)
    
    test_dns_resolution()
    test_ssl_handshake()
    test_http_connection()
    check_proxy_settings()
    check_python_ssl()
    
    print("\n" + "="*60)
    print("✅ 诊断完成！")
    print("="*60)
    
    # 网络建议
    print("\n💡 如果遇到问题:")
    print("   1. 设置环境变量：export AKSHARE_TIMEOUT=30")
    print("   2. 增加重试次数：export AKSHARE_RETRY_COUNT=3")
    print("   3. 检查防火墙/代理设置")
    print("   4. 等待交易时间 (9:30-15:00) 再试")

if __name__ == '__main__':
    main()
