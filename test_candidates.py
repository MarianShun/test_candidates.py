import pytest
from candidates import Candidate
maxid = 2100

@pytest.mark.parametrize('cid', range(2064,maxid))
def test_candidate_status_code_get(cid):
    assert Candidate().get(cid).status_code == 200

class TestsPostDel:
    names = ['QA Trainee', 'QA Intern', 'Junior QA', 'QA Engineer', 'Junior Automation QA', 'Delete']  
    @pytest.mark.parametrize(('position'), names)	
    def test_candidate_status_code_post(self, position):
        assert Candidate().post('Marian Shun', position).status_code == 201
		
    def test_candidate_status_code_del(self):
        assert Candidate().delete(maxid+6).status_code == 200
