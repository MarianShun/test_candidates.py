import pytest
from candidates import Candidate
maxid = 1185

@pytest.mark.parametrize('cid', range(1129,maxid))
class TestsGet:
    def test_candidate_status_code_get(self, cid):
        assert Candidate().get(cid).status_code == 200
    def test_candidate_content_get(self, cid):
        assert Candidate().get(cid).json()

names = ['QA Trainee', 'QA Intern', 'Junior QA', 'QA Engineer', 'Junior Automation QA', 'Delete']  
@pytest.mark.parametrize(('position'), names)
class TestsPost:
    def test_candidate_status_code_post(self, position):
        assert Candidate().post('Marian Shun', position).status_code == 201	
    def test_candidate_status_code_post(self, position):
        assert Candidate().post('Marian Shun', position).json()

def test_candidate_status_code_del():
    assert Candidate().delete(maxid+12).status_code == 200
