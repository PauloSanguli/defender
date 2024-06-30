import requests
import ssl
import socket
import urllib.parse
import email.utils
#import dns.resolver
analise=[]

from  threading import  Thread

def domonio_de_terceiro(url):
    tunnel_domains = [
        "ngrok.app", "ngrok.dev", "ngrok-free.app",  # Ngrok
        "cloudflare.com", "trycloudflare.com", "cloudflared.io",  # Cloudflare
        "localhost.run",  # Localhost.run
        "expose.dev",  # Expose
        "boringtun.io",  # BoringTun
        "pagekite.net",  # Pagekite
        "inconshreveable.com",  # Ngrok custom domain
        "tunnel.sh",  # Tunnel.sh
        "forwardhq.com",  # ForwardHQ
        "localtunnel.me",  # LocalTunnel
        "hostinger.com",  # Hostinger
        "dreamhost.com",  # DreamHost
    ]
    hostname = urllib.parse.urlparse(url).hostname
    for domain in tunnel_domains:
        if domain in hostname:

            return  True, "este  saite  não é  seguro  pertence  a dominio  de terceiro "

    return False


def vetor_de_ataque_move(url):
    adult_content_domains = [
        "pornhub.com",  # Pornhub
        "xvideos.com",  # Xvideos
        "xnxx.com",  # Xnxx
        "redtube.com",  # Redtube
        "youporn.com",  # Youporn
        "adultfriendfinder.com",  # AdultFriendFinder
        "ashleymadison.com",  # AshleyMadison
        "stripchat.com",  # StripChat
        "chaturbate.com",  # Chaturbate
        "camsoda.com",  # CamSoda
        "brazzers"
    ]
    hostname = urllib.parse.urlparse(url).hostname
    for domain in adult_content_domains:
        if domain in hostname:
            try:
              return True, "esta   associados  a conteudo  adulto"
            except:
                pass

    return False


def validar_link(url):
    api_key = "79c01aa90bef42976c4a1a5d50dea74ef5959674e6339bfb6b84aa943e0a4056"
    headers = {"x-apikey": api_key}
    response = requests.post("https://www.virustotal.com/api/v3/urls", headers=headers, json={"url": url})
    if response.status_code == 200:
        result = response.json()
        if result["data"]["attributes"]["last_analysis_stats"]["malicious"] > 0:
            return False
    else:
        return False

    if domonio_de_terceiro(url):
        return False

    if vetor_de_ataque_move(url):
        return False

    try:
        ssl_cert = ssl.get_server_certificate((url, 443))
        ssl_cert_info = ssl.DER_cert_to_PEM_cert(ssl_cert)
        ssl_cert_obj = ssl.load_certificate(ssl_cert_info)
        ssl_cert_subject = ssl_cert_obj.get_subject()
        if ssl_cert_subject.CN != url:
            return False
    except ssl.SSLError:
        return False

    return  True , "  este  saite  possui  certificado  ssl  "











