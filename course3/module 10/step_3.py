def sourcetemplate(url):
    def load(**kwargs):
        ans = ""
        if len(kwargs) == 0:
            ans = url
        if len(kwargs) > 0:
            ans = url + '?'
            for i in sorted(kwargs):
                ans += str(i) + '=' + str(kwargs[i]) + '&'
            ans = ans[:-1]
        return ans
    return load