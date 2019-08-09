class Solution {
public:
    bool isMatch(string s, string p) {
        return aux (s,p,0,0);
    }
    
    bool aux (string s, string p, int i1, int i2) {
        if (s.size() == i1 && p.size() == i2) {
            return true;
        } else if (s.size() == i1) {
            for (int i=i2;i<p.size();i++){
                if (p[i]!='*'){
                    return false;
                }
            }
            return true;
        }
        
        if (p[i2]=='*') {
            return aux (s,p,i1+1,i2+1) || aux (s,p,i1,i2+1) || aux (s,p,i1+1,i2);
        } else if (s[i1]!=p[i2] && p[i2] != '?'){
            return false;
        }
        
        return aux (s,p,i1+1,i2+1);
        
    }
};
