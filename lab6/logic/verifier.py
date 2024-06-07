class Verifier:

    def __init__(self):
        self.n = None
        self.x = None
        self.y = None

    def perform_validation(self):
        print("\nPerforming cleanup/validation")
        EPS = 0.00000001
        pts = []
        for i in range(self.n):
            pts.append([self.x[i], self.y[i]])
        pts = sorted(pts)
        for i in range(self.n):
            if pts[i][0] == 0:
                pts[i][0] = EPS

        used = []
        new_pts = []
        for p in pts:
            if p[0] not in used:
                new_pts.append(p)
                used.append(p[0])

        pts = new_pts
        x = []
        y = []
        n = 0
        for p in pts:
            x.append(p[0])
            y.append(p[1])
            n += 1

        if n <= 2:
            print("\nToo few points after cleanup! Terminating...")
            raise Exception
        print("\nValidation complete!")
        self.n = n
        self.x = x
        self.y = y
